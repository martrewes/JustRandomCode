# SleepTimer

A simple python (and QT) app to sleep, hibernate, reboot or shutdown a system.

I made this to compliment a refurbished Surface Pro (hence simple UI) that I had recently purchased. All of the apps I found either didn't work, weren't optimized for touch, or ran on Electron. (Granted, the libraries for this will be quite large also, but I use Python anyway.)

Should work on Windows and Linux.

## Requirements
```bash
pip install PyQt5

python main.py
```

## HiDPI

If you're not using a HiDPI screen, comment out:
```python
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
```

## TODO

- [ ] Make the dial and spinbox react to the time decreasing.
- [x] Okay I need to fix the UI on windows, it's pretty awful (see screenshot)

## Screenshot

![img](Screenshot.jpg) ![img](ScreenshotWindows.jpg)
