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


class Airport(PCM.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
       

        self.pushButton.clicked.connect(self.Enter)
        self.pushButton_2.clicked.connect(self.guest)
        self.pushButton_3.clicked.connect(self.Exit)
        
        
    def Enter(self):
        
        if self.lineEdit_Login.text() == "1" and self.lineEdit_Pass.text() =="1":
            self.sw = derector()
            self.sw.show()
        else:
            QMessageBox.critical(self, "ОШИБКА", "Логин или пароль не верный")
            self.sw = Captcha()
            self.sw.show()
            

    def guest(self):
        self.sw = prog()
        self.sw.show()

    
    def Dobav(self):
        self.go = spisok()
        self.sw.show()
        
    def Exit(self):
        exe.close()

    


class Captcha(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        layout  = QVBoxLayout()
        self.captcha_lbl = QLabel("Введите капчу:")
        self.captcha_box= QLineEdit()
        self.timer_lbl = QLabel("Таймер:10")
        self.capth_ver = QPushButton("Проверить")
        self.captcha_ran = QLabel(str(random.randint(1000,9000)))
        
        self.timer = QTimer()
        self.count = 10
        self.timer_lbl.setText(str(self.count))
        self.timer.timeout.connect(self.timer_tick)
        
        
        
        layout.addWidget(self.captcha_lbl)
        layout.addWidget(self.captcha_ran)
        layout.addWidget(self.captcha_box)
        layout.addWidget(self.timer_lbl)
        layout.addWidget(self.capth_ver)
        
        self.capth_ver.clicked.connect(self.ver)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def ver (self):
            
        
        if self.captcha_box.text() == self.captcha_ran.text():
            QMessageBox.information(self, "Успех", "Капча введена правильно")
            Captcha.close(self)
            
            
        else:
            self.captcha_box.setDisabled(True)
            self.timer.start()
            QMessageBox.critical(self, "ОШИБКА", "Вы ввели неправильно")
            
            
        
            
    def timer_tick(self):
        self.timer.start(1000)
        self.count -=1
        self.timer_lbl.setText(str(self.count))
        
        if  self.count == 0:
            self.timer.stop()
            self.captcha_box.setDisabled(False)

app = QApplication(sys.argv)
exe = Airport()
exe.show()
app.exec()