

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class prog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        
        self.setupUi(self)
        db = QSqlDatabase.addDatabase('QPSQL')
        db.setDatabaseName('progect')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setUserName('postgres')
        db.setPassword('student')
        db.open()

        

        queru = QSqlTableModel()
        sql ="SELECT * FROM public.projects"
        queru.setQuery(QSqlQuery(sql))
        print(QSqlQuery(sql).isActive())
        self.tableView.setModel(queru)
        self.tableView.setColumnHidden(0, True)

        # if queru.isActive():
        #     print("ok")
        # else:
        #     print("No")



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(218, 207, 183);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 70, 761, 381))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(679, 490, 101, 26))
        self.pushButton.setStyleSheet("background-color: rgba(77, 168, 4, 213);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 490, 80, 26))
        self.pushButton_2.setStyleSheet("background-color: rgba(140, 3, 3, 190);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 0, 351, 51))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.Exit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Просмотреть "))
        self.pushButton_2.setText(_translate("MainWindow", "Выход"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; font-style:italic;\">Проекты </span></p></body></html>"))

    def Exit(self):
        self.close()

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from spisok import spisoc

class derector(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setupUi(self)
        db = QSqlDatabase.addDatabase('QPSQL')
        db.setDatabaseName('progect')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setUserName('postgres')
        db.setPassword('student')
        db.open()

        

        queru = QSqlTableModel()
        sql ="SELECT * FROM public.projects"
        queru.setQuery(QSqlQuery(sql))
        print(QSqlQuery(sql).isActive())
        self.tableView.setModel(queru)
        self.tableView.setColumnHidden(0, True)


        self.pushButton_Exit.clicked.connect(self.Exit)
        self.pushButton_dobav.clicked.connect(self.Dobav)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Exit.setText(_translate("MainWindow", "Выход"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:400;\">Director</span></p></body></html>"))
        self.pushButton_prosmtr.setText(_translate("MainWindow", "Посмотреть "))
        self.pushButton_delete.setText(_translate("MainWindow", "Удалить"))
        self.label_2.setText(_translate("MainWindow", "Вы авторизировались как руководитель проекта"))
        self.pushButton_dobav.setText(_translate("MainWindow", "Добавить"))

    def Exit(self):
        self.close()

    def Dobav(self):
        self.go = spisoc(self.tableView)
        self.go.setupUi(self.go)
        self.go.show()