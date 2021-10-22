from os import close
import datetime
from decimal import *
while True:
    try:
        with open('/home/username/.config/quodlibet/current') as f:

            lines = f.readlines()
            for line in lines:
                if "artist=" in line:
                    artist = line[7:-1]
                if "album=" in line:
                    album = line[6:-1]
                if "title=" in line:
                    title = line[6:-1]
                if "date=" in line:
                    if len(line) > 9:
                        date = line[5:9]
                    else:
                        date = line[5:]
                if "tracknumber=" in line:
                    track = line[12:]
                if "~#length=" in line:
                    ltemp = round(Decimal(line[9:-1]))
                    lengthTemp = "(" + str(datetime.timedelta(seconds=ltemp))[2:] + ")"
                    


            
            print(str(track[:-1]) + ". " + title + " " + str(lengthTemp), '\n' + artist + " - " + album + " [" + date + "]")
            exit()

    except FileNotFoundError:

        print("Not playing")
        print("any audio")
        exit()

