import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import auth, reg, db2, capcha
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel, QSqlQuery
import random

class Auth(auth.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.edit_login.setPlaceholderText('Введите логин:')
        self.edit_password.setPlaceholderText('Введите пароль:')
        self.btn_reg.clicked.connect(self.reg)
        self.btn_auth.clicked.connect(self.auth)
        self.btn_exit.clicked.connect(self.exit)

    
        db = QSqlDatabase.addDatabase('QPSQL')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setDatabaseName('test')
        db.setUserName('postgres')
        db.setPassword('student')
        db.open()

        query = QSqlQuery()
        sql = "SELECT * FROM public.user"
        data = query.exec(sql)

        if query.isActive():
            print('OK')
        else:
            print('NO')

        self.login = []
        self.password = []
        query.first()
        while query.isValid():
            
            self.login.append(query.value('login'))
            self.password.append(query.value('password'))
            query.next()
    def auth(self):
        
        for l in (range(len(self.login))):
            for p in (range(len(self.password))):
                if self.edit_login.text() == self.login[l] and self.edit_password.text() == self.password[p] and l == p:
                    self.main = Capcha()
                    self.main.show()
                    self.close()
                   
    def reg(self):
        self.main = Reg()
        self.main.show()
        self.close()

    def exit(self):
        self.close()

class Reg(reg.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_auth.clicked.connect(self.auth)
        self.btn_exit.clicked.connect(self.exit)

    def auth(self):
        self.main = Auth()
        self.main.show() 
        self.close()

    def exit(self):
        self.close()

class Db(db2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_nazad.clicked.connect(self.nazad)
        self.btn_exit.clicked.connect(self.exit)
        self.btn_poisk.clicked.connect(self.poisk)

        db = QSqlDatabase.addDatabase('QPSQL')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setDatabaseName('name')
        db.setUserName('postgres')
        db.setPassword('student')
        db.open()

        query = QSqlQuery()
        sql = "SELECT * FROM public.rus"
        query.exec(sql)

        stm = QSqlTableModel()
        stm.setTable('rus')
        stm.select()
        self.tableView.setModel(stm)

        sqm = QSqlQueryModel(parent=self.tableView)
        sql_select = 'select * from public.rus'
        sqm.setQuery(sql_select)
        self.tableView.setModel(sqm)

        self.click = 1
        

    def nazad(self):
        self.main = Auth()
        self.main.show()
        self.close()
    def exit(self):
        self.close()
    
    
    def poisk(self):
        self.click += 1
        if self.click==2:

            query = QSqlQuery()
            sql = "SELECT * FROM public.eng"
            query.exec(sql)

            stm = QSqlTableModel()
            stm.setTable('eng')
            stm.select()
            self.tableView.setModel(stm)

            sqm = QSqlQueryModel(parent=self.tableView)
            sql_select = 'select * from public.eng'
            sqm.setQuery(sql_select)
            self.tableView.setModel(sqm)
            self.btn_poisk.setText('RU')
            self.click =0
        if self.click ==1:
            query = QSqlQuery()
            sql = "SELECT * FROM public.rus"
            query.exec(sql)

            stm = QSqlTableModel()
            stm.setTable('rus')
            stm.select()
            self.tableView.setModel(stm)

            sqm = QSqlQueryModel(parent=self.tableView)
            sql_select = 'select * from public.rus'
            sqm.setQuery(sql_select)
            self.tableView.setModel(sqm)
            self.btn_poisk.setText('EN')
            







class Capcha(capcha.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lbl_capcha.setText(str(random.randint(1000,9999)))
        self.btn.clicked.connect(self.capcha)
    def capcha(self):
        if self.edit_capcha.text() == self.lbl_capcha.text():
            self.main = Db()
            self.main.show()
            self.close()
        else:
            self.lbl_capcha.setText(str(random.randint(1000,9999)))
            self.btn.blockSignals(True)
            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.timer_tick)
            self.second = 11
            self.timer.start()
            
    def timer_tick(self):
        self.second -= 1
        self.lbl_timer.setText(str(self.second))
        if self.second == 0:
            self.timer.stop()
            self.lbl_timer.setText('')
            self.btn.blockSignals(False)
app = QApplication(sys.argv)
window = Db()
window.show()
app.exec()     