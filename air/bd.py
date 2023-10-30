import sys
from PyQt5.QtSql import QSqlDatabase,QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import *
import PCM
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from progeckt import prog
from PyQt5.QtCore import *
import random
from Derector import derector
import spisok
from Manager import Managers
from captcha import Captcha
from admin import Admin


class Airport(PCM.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        db = QSqlDatabase.addDatabase('QPSQL')
        db.setDatabaseName('progect')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setUserName('postgres')
        db.setPassword('student')
        db.open()

        self.setupUi(self)
       

        self.pushButton.clicked.connect(self.Enter)
        self.pushButton_2.clicked.connect(self.guest)
        self.pushButton_3.clicked.connect(self.Exit)
        self.pushButton_4.clicked.connect(self.Admin)
        
    def Enter(self):
        query = QSqlQuery()
        query.exec(f"SELECT * FROM public.staff WHERE login = '{self.lineEdit_Login.text()}' AND password = '{self.lineEdit_Pass.text()}'")
        if query.first():
            if query.value(3) == 2:
                self.sw = derector()
                self.sw.show()
            elif query.value(3) == 1:
                self.sw = Managers()
                self.sw.show()
            # elif self.lineEdit_Login.text() =="Admin" and self.lineEdit_Pass.text() =="Admin":
            #     self.sw = Admin()
            #     self.sw.show()
        else:
            QMessageBox.critical(self, "ОШИБКА", "Логин или пароль не верный")
            self.sw = Captcha()
            self.sw.setupUi(self.sw)
            self.sw.show()
            

    def guest(self):
        self.sw = prog()
        self.sw.show()

    
    def Dobav(self):
        self.go = spisok()
        self.sw.show()
        
    def Exit(self):
        exe.close()
    
    def Admin(self):
        if self.lineEdit_Login.text() == "Admin" and self.lineEdit_Pass.text() =="Admin":
            self.sw = Admin()
            self.sw.setupUi(self.sw)
            self.sw.show()

    


# class Captcha(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         self.setWindowFlags(Qt.FramelessWindowHint)
#         layout  = QVBoxLayout()
#         self.captcha_lbl = QLabel("Введите капчу:")
#         self.captcha_box= QLineEdit()
#         self.timer_lbl = QLabel("Таймер:10")
#         self.capth_ver = QPushButton("Проверить")
#         self.captcha_ran = QLabel(str(random.randint(1000,9000)))
        
#         self.timer = QTimer()
#         self.count = 10
#         self.timer_lbl.setText(str(self.count))
#         self.timer.timeout.connect(self.timer_tick)
        
        
        
#         layout.addWidget(self.captcha_lbl)
#         layout.addWidget(self.captcha_ran)
#         layout.addWidget(self.captcha_box)
#         layout.addWidget(self.timer_lbl)
#         layout.addWidget(self.capth_ver)
        
#         self.capth_ver.clicked.connect(self.ver)
        
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)
    
#     def ver (self):
            
        
#         if self.captcha_box.text() == self.captcha_ran.text():
#             QMessageBox.information(self, "Успех", "Капча введена правильно")
#             Captcha.close(self)
            
            
#         else:
#             self.captcha_box.setDisabled(True)
#             self.timer.start()
#             QMessageBox.critical(self, "ОШИБКА", "Вы ввели неправильно")
            
            
        
            
#     def timer_tick(self):
#         self.timer.start(1000)
#         self.count -=1
#         self.timer_lbl.setText(str(self.count))
        
#         if  self.count == 0:
#             self.timer.stop()
#             self.captcha_box.setDisabled(False)

    

app = QApplication(sys.argv)
exe = Airport()
exe.show()
app.exec()



# q = f"SELECT * FROM public.staff"
        # print(q)
        # queru = QSqlQuery(q)
        # print(queru.isActive())
        # queru.exec()
        # print(queru.first())
        # if queru.first():
        #     self.sw = derector()
        #     self.sw.show()
