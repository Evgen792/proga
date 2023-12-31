from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Prosmotr(QMainWindow):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 658)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_close2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close2.setGeometry(QtCore.QRect(10, 620, 81, 31))
        self.pushButton_close2.setStyleSheet("background-color: rgba(206, 108, 108, 170);")
        self.pushButton_close2.setObjectName("pushButton_close2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 50, 731, 531))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.lineEdit_text.setFont(font)
        self.lineEdit_text.setStyleSheet("font: 25 14pt \"URW Bookman\";")
        self.lineEdit_text.setText("")
        self.lineEdit_text.setObjectName("lineEdit_text")
        self.gridLayout.addWidget(self.lineEdit_text, 1, 1, 1, 1)
        self.Label_text = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.Label_text.setFont(font)
        self.Label_text.setObjectName("Label_text")
        self.gridLayout.addWidget(self.Label_text, 1, 0, 1, 1)
        self.Ladel_manage = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.Ladel_manage.setFont(font)
        self.Ladel_manage.setObjectName("Ladel_manage")
        self.gridLayout.addWidget(self.Ladel_manage, 3, 0, 1, 1)
        self.Label_director = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.Label_director.setFont(font)
        self.Label_director.setObjectName("Label_director")
        self.gridLayout.addWidget(self.Label_director, 2, 0, 1, 1)
        self.Ladel_change = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.Ladel_change.setFont(font)
        self.Ladel_change.setObjectName("Ladel_change")
        self.gridLayout.addWidget(self.Ladel_change, 4, 0, 1, 1)
        self.lineEdit_director = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.lineEdit_director.setFont(font)
        self.lineEdit_director.setStyleSheet("font: 25 14pt \"URW Bookman\";")
        self.lineEdit_director.setText("")
        self.lineEdit_director.setObjectName("lineEdit_director")
        self.gridLayout.addWidget(self.lineEdit_director, 2, 1, 1, 1)
        self.Label_index = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.Label_index.setFont(font)
        self.Label_index.setObjectName("Label_index")
        self.gridLayout.addWidget(self.Label_index, 7, 0, 1, 1)
        self.Label_city = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.Label_city.setFont(font)
        self.Label_city.setObjectName("Label_city")
        self.gridLayout.addWidget(self.Label_city, 5, 0, 1, 1)
        self.Label_name = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.Label_name.setFont(font)
        self.Label_name.setObjectName("Label_name")
        self.gridLayout.addWidget(self.Label_name, 0, 0, 1, 1)
        self.Label_street = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.Label_street.setFont(font)
        self.Label_street.setObjectName("Label_street")
        self.gridLayout.addWidget(self.Label_street, 6, 0, 1, 1)
        self.lineEdit_manage = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.lineEdit_manage.setFont(font)
        self.lineEdit_manage.setStyleSheet("font: 25 14pt \"URW Bookman\";")
        self.lineEdit_manage.setText("")
        self.lineEdit_manage.setObjectName("lineEdit_manage")
        self.gridLayout.addWidget(self.lineEdit_manage, 3, 1, 1, 1)
        self.lineEdit_change = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.lineEdit_change.setFont(font)
        self.lineEdit_change.setStyleSheet("font: 25 14pt \"URW Bookman\";")
        self.lineEdit_change.setText("")
        self.lineEdit_change.setObjectName("lineEdit_change")
        self.gridLayout.addWidget(self.lineEdit_change, 4, 1, 1, 1)
        self.lineEdit_city = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.lineEdit_city.setFont(font)
        self.lineEdit_city.setStyleSheet("font: 25 14pt \"URW Bookman\";")
        self.lineEdit_city.setText("")
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.gridLayout.addWidget(self.lineEdit_city, 5, 1, 1, 1)
        self.lineEdit_street = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.lineEdit_street.setFont(font)
        self.lineEdit_street.setStyleSheet("font: 25 14pt \"URW Bookman\";")
        self.lineEdit_street.setText("")
        self.lineEdit_street.setObjectName("lineEdit_street")
        self.gridLayout.addWidget(self.lineEdit_street, 6, 1, 1, 1)
        self.lineEdit_index = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.lineEdit_index.setFont(font)
        self.lineEdit_index.setStyleSheet("font: 25 14pt \"URW Bookman\";")
        self.lineEdit_index.setText("")
        self.lineEdit_index.setObjectName("lineEdit_index")
        self.gridLayout.addWidget(self.lineEdit_index, 7, 1, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("font: 25 14pt \"URW Bookman\";")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-2, -3, 831, 661))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(190, 179, 159);\n"
"border-radius: 20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_Close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Close.setGeometry(QtCore.QRect(780, 10, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_Close.setFont(font)
        self.pushButton_Close.setStyleSheet("background-color: rgb(190, 179, 159);\n"
"border-radius:px20;")
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.label.raise_()
        self.pushButton_close2.raise_()
        self.gridLayoutWidget.raise_()
        self.pushButton_Close.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_close2.setText(_translate("MainWindow", "Назад"))
        self.Label_text.setText(_translate("MainWindow", "Описание"))
        self.Ladel_manage.setText(_translate("MainWindow", "Менеджер проекта"))
        self.Label_director.setText(_translate("MainWindow", "Руководитель проекта"))
        self.Ladel_change.setText(_translate("MainWindow", "Изминение проекта"))
        self.Label_index.setText(_translate("MainWindow", "Индекс"))
        self.Label_city.setText(_translate("MainWindow", "Город"))
        self.Label_name.setText(_translate("MainWindow", "Название проекта"))
        self.Label_street.setText(_translate("MainWindow", "Улица"))
        self.pushButton_Close.setText(_translate("MainWindow", "✕"))

        
