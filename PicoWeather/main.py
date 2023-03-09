import badger2040w
import jpegdec
import utime
import machine
import ntptime
from badger2040w import WIDTH
import urequests
import ahtx0
import machine

# Create I2C object

# Print out any addresses found


badger = badger2040w.Badger2040W()
jpeg = jpegdec.JPEG(badger.display)
badger2040w.system_speed(3)
badger.set_update_speed(1)



try:
    badger.connect()
    if badger.isconnected():
        ntptime.settime()
except (RuntimeError, OSError):
    pass  # no WiFI

LAT = 51.491879
LNG = -0.082484
TIMEZONE = "auto"  # determines time zone from lat/long
URL = "http://api.open-meteo.com/v1/forecast?latitude=" + str(LAT) + "&longitude=" + str(LNG) + "&current_weather=true&timezone=" + TIMEZONE


wifiIP = badger2040w.network.WLAN(badger2040w.network.STA_IF).ifconfig()[0]
rtc = machine.RTC()
badger.led(128)
def clearScreen():
    badger.set_pen(15)
    badger.clear()
    badger.set_pen(0)

def scanI2C():
    devices = i2c.scan()
    if devices:
        for d in devices:
            print((d))

def drawRec(startX,startY,xSize,ySize):
    badger.line(startX,startY,xSize,startY)
    badger.line(startX,startY,startX,startY + ySize)
    badger.line(startX+xSize,startY,startX+xSize,startY+ySize)
    badger.line(startX,startY+ySize,startX+xSize,startY+ySize)
    #	 A
    #	---
    # B|   |C
    #	---
    #    D

def get_data():
    global weathercode, temperature, windspeed, winddirection, date, time
    print(f"Requesting URL: {URL}")
    r = urequests.get(URL)
    # open the json data
    j = r.json()
    print("Data obtained!")
    print(j)

    # parse relevant data from JSON
    current = j["current_weather"]
    temperature = current["temperature"]
    windspeed = current["windspeed"]
    winddirection = calculate_bearing(current["winddirection"])
    weathercode = current["weathercode"]
    date, time = current["time"].split("T")

    r.close()

def calculate_bearing(d):
    # calculates a compass direction from the wind direction in degrees
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    ix = round(d / (360. / len(dirs)))
    return dirs[ix % len(dirs)]

def getTime():
    
    urlTime = "http://worldtimeapi.org/api/timezone/Europe/London" # see http://worldtimeapi.org/timezones

    response = urequests.get(urlTime)
    
    if response.status_code == 200: # query success
        
        print("JSON response:\n", response.text)
            
            # parse JSON
        parsed = response.json()
        datetime_str = str(parsed["datetime"])
        year = int(datetime_str[0:4])
        month = int(datetime_str[5:7])
        day = int(datetime_str[8:10])
        hour = int(datetime_str[11:13])
        minute = int(datetime_str[14:16])
        second = int(datetime_str[17:19])
        subsecond = int(round(int(datetime_str[20:26]) / 10000))
    
        # update internal RTC
        rtc.datetime((year, month, day, 0, hour, minute, second, subsecond))
        update_time = utime.ticks_ms()
        print("RTC updated\n")

    #rtc = machine.RTC()
def updateTime():    
    year, month, day, wd, hour, minute, second, _ = rtc.datetime()
    hours = "{:02}".format(hour)
    mins = "{:02}".format(minute)
    dmy = "{:02}/{:02}/{:02}".format(day, month, year)

    
    #print(rtc.datetime)
    badger.set_thickness(2)
    badger.set_font("sans")
    badger.text("-- Time & Date --",8,124,scale=0.4, angle=270)
    #drawRec(60,4,130,90)
    badger.set_thickness(5)
    badger.set_font("serif")
    badger.text(hours, 40, 124, scale=1.2, angle=270)
    badger.text(mins, 52, 82, scale=2, angle=270)
    badger.set_font("sans")
    badger.set_thickness(2)
    badger.text(dmy, 82, 124, scale=0.6, angle=270)

def setWifi():
    badger.set_pen(0)
    badger.set_thickness(1)
    badger.set_font("sans")
    badger.text("WiFi: " + wifiIP, 288, 124,scale=0.4, angle=270)

def setWeather():
    if temperature is not None:
        badger.set_thickness(2)
        badger.set_font("sans")
        badger.text("--   Weather   --",102,124,scale=0.4, angle=270)
        # Choose an appropriate icon based on the weather code
        # Weather codes from https://open-meteo.com/en/docs
        # Weather icons from https://fontawesome.com/
        if weathercode in [71, 73, 75, 77, 85, 86]:  # codes for snow
            jpeg.open_file("/icons/icon-snow.jpg")
        elif weathercode in [51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 80, 81, 82]:  # codes for rain
            jpeg.open_file("/icons/icon-rain.jpg")
        elif weathercode in [1, 2, 3, 45, 48]:  # codes for cloud
            jpeg.open_file("/icons/icon-cloud.jpg")
        elif weathercode in [0]:  # codes for sun
            jpeg.open_file("/icons/icon-sun.jpg")
        elif weathercode in [95, 96, 99]:  # codes for storm
            jpeg.open_file("/icons/icon-storm.jpg")
        jpeg.decode(116, 90, jpegdec.JPEG_SCALE_HALF)
        badger.set_pen(0)
        badger.set_font("sans")
        badger.set_thickness(4)
        badger.text(f"{temperature}", 132,88, scale=1.1, angle=270)
        badger.set_thickness(2)
        badger.text("°",118,14, scale=0.6, angle=270)
        badger.text("C",136,18,scale=0.8,angle=270)
        mphTemp = windspeed * 0.621371
        mph = "{:.1f}".format(mphTemp)
        badger.text(f"{mph}" + "mph | " + f"{winddirection}",158, 112, scale=0.5,angle=270)
    #    badger.text(f"Wind Direction: {winddirection}", int(WIDTH / 3), 68, WIDTH - 105, 2)
    #    badger.text(f"Last update: {date}, {time}", int(WIDTH / 3), 88, WIDTH - 105, 2)

    else:
        badger.set_pen(0)
        badger.rectangle(0, 60, WIDTH, 25)
        badger.set_pen(15)
        badger.text("Unable to badger weather! Check your network settings in WIFI_CONFIG.py", 5, 65, WIDTH, 1)

def setIntTemp():
    i2c = machine.I2C(0, scl=machine.Pin(5), sda=machine.Pin(4))  
    sensor = ahtx0.AHT10(i2c)
    inTemp = "%0.2f" % sensor.temperature
    inHum = "%0.2f%%" % sensor.relative_humidity

    badger.text("--   Internal   --",178,124,scale=0.4, angle=270)
    badger.set_thickness(4)
    badger.text(inTemp, 204,122, scale=1.1, angle=270)
    badger.set_thickness(2)
    badger.text("°",192,14, scale=0.6, angle=270)
    badger.text("C",210,18,scale=0.8,angle=270)
        
    
while True:
    clearScreen()
    get_data()
    updateTime()
    setWifi()
    setWeather()
    setIntTemp()
    #Help

    badger.update()
    utime.sleep(5)
