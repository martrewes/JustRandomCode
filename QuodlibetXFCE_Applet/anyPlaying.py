#!/usr/bin/env python3
import datetime
import dbus
import urllib.parse
from PIL import Image

bus = dbus.SessionBus()
noPlayer = False

for service in bus.list_names():
    
    if service.startswith('org.mpris.MediaPlayer2.'):
        
        player = dbus.SessionBus().get_object(service, '/org/mpris/MediaPlayer2')
        status=player.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
        metadata = player.Get('org.mpris.MediaPlayer2.Player', 'Metadata', dbus_interface='org.freedesktop.DBus.Properties')
        #print(metadata)

        #print no media playing if nothing is in fact, playing
        if status == "Paused" or status == "Stopped":
            print(" No media")
            print(" currently playing")
            quit()
        
        else:
        #Get song information
            try:
                title = str(metadata["xesam:title"])
            except KeyError:
                title = ""

            try:
                artist = str(metadata["xesam:artist"][0])
            except KeyError:
                artist = ""

            try:
                album = str(metadata["xesam:album"])
            except KeyError:
                album = ""
            
            try:
                year = " [" + str(metadata["xesam:contentCreated"][0:4]) + "]"
            except KeyError:
                year = ""

            baseTime = datetime.datetime(1,1,1)
            try:
                lengthTemp = datetime.timedelta(seconds=(metadata["mpris:length"]) / 1000000)
                length = " (" + (baseTime+lengthTemp).strftime('%M:%S') + ")"
            except KeyError:
                length = ""

            try:
                trackNo = str(metadata["xesam:trackNumber"]) + ". "
            except KeyError:
                trackNo = ""
            
            try:
                artUrl = urllib.parse.unquote(str(metadata["mpris:artUrl"][7:]))
            except KeyError:
                artUrl = ""

            #create the strings
            strLine1 = trackNo + title + length
            strLine2 = (artist + " - " + album + year)
            
            #add padding on either - no longer seem to need

            #if len(strLine1) < len(strLine2):
            #    padding = round((len(strLine2) - len(strLine1)) / 4)
            #    strLine1 = " " * padding + strLine1
            #    
            #else:
            #    padding = round((len(strLine1) - len(strLine2)) / 2)
            #    strLine2 = " " * padding + strLine2
            
            #resize the art
            if artUrl != "":
                baseheight = 48
                img = Image.open(artUrl)
                hpercent = (baseheight / float(img.size[1]))
                wsize = int((float(img.size[0]) * float(hpercent)))
                img = img.resize((wsize, baseheight))
                img.save('/tmp/albumArt.jpg')
                artUrl = '<img>/tmp/albumArt.jpg</img>'
           
            print(artUrl + "<txt> " + strLine1 + "\n " + strLine2 + "</txt>")
           

            
        quit()
    else:
        noPlayer = True
    
if noPlayer == True:
    print("")
    print("")