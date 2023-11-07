
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *


class Vxod(QMainWindow):
    def setupUi(self, MainWindow):
        # self.setupUi(self)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 557)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 601, 571))
        self.label.setStyleSheet("border-radius: 50px;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Other-Trainings.jpg"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


    def timer_tick(self):
        self.timer.start(1000)
        self.count -=1
        self.label_Time.setText(str(self.count))
        
        if  self.count == 0:
            self.timer.stop()
            self.count =10
            self.lineEdit_kapcha.setDisabled(False)    
