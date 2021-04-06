import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

mydb = mysql.connector.connect(
  host="000.000.000.000",
  port="3306",
  user="esp_board",
  password="OpenMCUPass",
  database="esp_data"
)

temp = mydb.cursor()

temp.execute("SELECT * FROM Sensor")
tempArr = temp.fetchall()
tempList = []
timeList = []
#time.execute("SELECT reading_time FROM Sensor")
#timeArr = time.fetchall()
#for each in tempList:
#    each.strip("()'")
for tempRow in tempArr:
    tempList.append(tempRow[1])
for timeRow in tempArr:
    timeList.append(timeRow[5])

# print (timeArr)
# Create data


# Area plot
plt.plot(timeList,tempList)
plt.show()