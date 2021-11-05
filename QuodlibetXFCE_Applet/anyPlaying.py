#!/usr/bin/env python3
import datetime
import dbus
#from mpris2 import Player

bus = dbus.SessionBus()
noPlayer = False

for service in bus.list_names():
    #print(service)
    if service.startswith('org.mpris.MediaPlayer2.'):
        #print(service)
        player = dbus.SessionBus().get_object(service, '/org/mpris/MediaPlayer2')
        status=player.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
        metadata = player.Get('org.mpris.MediaPlayer2.Player', 'Metadata', dbus_interface='org.freedesktop.DBus.Properties')
        
        if status == "Paused" or status == "Stopped":
            print("     No media")
            print(" currently playing")
            quit()
        
        else:
        #Get Globals
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

            strLine1 = trackNo + title + length
            strLine2 = (artist + " - " + album + year)
            
            if len(strLine1) < len(strLine2):
                padding = round((len(strLine2) - len(strLine1)) / 2)
                print(" " * padding + strLine1)
                print(strLine2)
            else:
                padding = round((len(strLine1) - len(strLine2)) / 2)
                print(strLine1)
                print(" " * padding + strLine2)#
            
            
        quit()
    else:
        noPlayer = True
    
if noPlayer == True:
    print("")
    print("")