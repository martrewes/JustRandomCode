from PyQt5 import QtWidgets, uic, QtCore
import sys
import os

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

class Ui(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.dial = self.findChild(QtWidgets.QDial, 'dialMins')
        self.dial.valueChanged.connect(self.sliderMoved)
        self.dial.setValue(30)
        self.dial.setMaximum(180)
        self.btnStart = self.findChild(QtWidgets.QPushButton, 'btnStart')
        self.btnUp = self.findChild(QtWidgets.QPushButton, 'btnUp')
        self.btnDown = self.findChild(QtWidgets.QPushButton, 'btnDown')
        self.spnTime = self.findChild(QtWidgets.QSpinBox, 'spnTime')
        self.groupBox = self.findChild(QtWidgets.QGroupBox, 'groupBox')
        self.statusBar = self.findChild(QtWidgets.QStatusBar, 'statusbar')
        self.radShutdown = self.findChild(QtWidgets.QRadioButton, 'radShutdown')
        self.radRestart = self.findChild(QtWidgets.QRadioButton, 'radRestart')
        self.radSleep = self.findChild(QtWidgets.QRadioButton, 'radSleep')
        self.radHibernate = self.findChild(QtWidgets.QRadioButton, 'radHibernate')
        self.btnStart.clicked.connect(self.btnPressed)
        self.btnUp.clicked.connect(self.btnChangeMinsUp)
        self.btnDown.clicked.connect(self.btnChangeMinsDown)
        self.spnTime.valueChanged.connect(self.timeChanged)
        self.active = False
        self.show()
        
    def sliderMoved(self):
        self.spnTime.setValue(int(self.dial.value()))
    
    def btnChangeMinsUp(self):
        self.spnTime.setValue(self.spnTime.value() + 1)
    
    def btnChangeMinsDown(self):
        self.spnTime.setValue(self.spnTime.value() - 1)

    def btnPressed(self):

        if self.active == False:
            self.btnStart.setText("Cancel")
            self.spnTime.setEnabled(False)
            self.dialMins.setEnabled(False)
            self.groupBox.setEnabled(False)
            self.active = True
            self.timer0 = QtCore.QTimer()
            self.time = QtCore.QTime(0, 0, 0)
            self.time = self.time.addSecs(int(self.spnTime.value()) * 60)
            self.timer0.setInterval(1000)
            self.timer0.timeout.connect(lambda:self.ticker())
            self.timer0.start()
        else:
            self.btnStart.setText("Set Timer")
            self.active = False
            self.spnTime.setEnabled(True)
            self.dialMins.setEnabled(True)
            self.groupBox.setEnabled(True)
            self.statusBar.clearMessage()

    def timeChanged(self):
        self.dial.setValue(self.spnTime.value())
    
    def ticker(self):
        if self.active == True:
            global time
            if self.time.second() == 0 and self.time.minute() == 0 and self.time.hour() == 0:
                if self.radShutdown.isChecked():
                    print("Shutdown!")
                    if os.name == 'nt':
                        os.system("shutdown /s /t 10")
                    else: 
                        os.system("systemctl poweroff")
                if self.radRestart.isChecked():
                    print("Restarting!")
                    if os.name == 'nt':
                        os.system("shutdown /r /t 10")
                    else:
                        os.system("systemctl reboot")
                if self.radSleep.isChecked():
                    print("Sleeping!")
                    if os.name == 'nt':
                        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                    else:
                        os.system("systemctl suspend")
                if self.radHibernate.isChecked():
                    print("Hibernating!")
                    if os.name == 'nt':
                        os.system("rundll32.exe powrprof.dll,SetSuspendState 1,1,0")
                    else:
                        os.system("systemctl hibernate")
                exit()
            self.time = self.time.addSecs(-1)
            self.statusBar.showMessage("Time Remaining: " + self.time.toString("hh:mm:ss",))
active = False
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
