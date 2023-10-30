from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Admin(QMainWindow):
     
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        
        db = QSqlDatabase.addDatabase('QPSQL')
        db.setDatabaseName('progect')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setUserName('postgres')
        db.setPassword('student')
        db.open()

        

        # queru = QSqlTableModel()
        # sql ="SELECT * FROM public.staff"
        # queru.setQuery(QSqlQuery(sql))
        # print(QSqlQuery(sql).isActive())
        # self.tableView.setModel(queru)
        # self.tableView.setColumnHidden(0, True)


        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(290, 387)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(199, 179, 151);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 0, 151, 51))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 40, 231, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_Login = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Login.setObjectName("lineEdit_Login")
        self.gridLayout.addWidget(self.lineEdit_Login, 0, 1, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 1, 1, 1, 1)
        self.pushButton_dobav = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dobav.setGeometry(QtCore.QRect(100, 280, 91, 26))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.pushButton_dobav.setFont(font)
        self.pushButton_dobav.setObjectName("pushButton_dobav")
        self.pushButton_Out = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Out.setGeometry(QtCore.QRect(100, 330, 91, 26))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.pushButton_Out.setFont(font)
        self.pushButton_Out.setObjectName("pushButton_Out")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton_Out.clicked.connect(self.Exit)
        self.pushButton_dobav.clicked.connect(self.Dobav)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Administrator"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_2.setText(_translate("MainWindow", "Login"))
        self.pushButton_dobav.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_Out.setText(_translate("MainWindow", "Выход"))

        self.lineEdit_password.setText(str(random.randint(100000,900000)))
        

    def Exit(self):
        self.close()

    def Dobav(self):
        q = f"INSERT INTO public.staff (login, password, role_id) VALUES ('{self.lineEdit_Login.text()}', '{self.lineEdit_password.text()}', '1')"
        # db = QSqlDatabase.addDatabase('QPSQL')
        # db.setDatabaseName('progect')
        # db.setHostName('localhost')
        # db.setPort(5432)
        # db.setUserName('postgres')
        # db.setPassword('student')
        # db.open()
        
        queru = QSqlQuery(q)
        print(queru.isActive())
        queru.exec()
        