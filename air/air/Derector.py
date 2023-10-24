

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

    

        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(218, 207, 183);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 421, 541))
        self.tableView.setObjectName("tableView")
        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setGeometry(QtCore.QRect(10, 560, 91, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.pushButton_Exit.setFont(font)
        self.pushButton_Exit.setStyleSheet("background-color: rgba(128, 37, 37, 57);")
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_prosmtr = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_prosmtr.setGeometry(QtCore.QRect(440, 160, 111, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.pushButton_prosmtr.setFont(font)
        self.pushButton_prosmtr.setObjectName("pushButton_prosmtr")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(440, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 40, 351, 51))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_dobav = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dobav.setGeometry(QtCore.QRect(440, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.pushButton_dobav.setFont(font)
        self.pushButton_dobav.setObjectName("pushButton_dobav")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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