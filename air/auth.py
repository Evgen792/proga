import sys
from window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from magaz import Magaz


class Auth(Ui_MainWindow):
    def __init__(self):
        super().__init__()


        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushButton_click)
        self.pushButton_2.clicked.connect(self.pushButton_click2)
        self.pushButton_3.clicked.connect(self.pushButton_click3)

        db = QSqlDatabase.addDatabase('QPSQL')
        db.setDatabaseName('test1')
        db.setHostName('localhost')
        db.setUserName('postgres')
        db.setPort(5432)
        db.setPassword('student')
        db.open()

        queru = QSqlQuery()
        sql_select ="SELECT * FROM public.test2"
        data = queru.exec(sql_select)

        if queru.isActive():
            print("ok")
        else:
            print("No")

        self.login=[]
        self.psw=[]

        queru.first()
        
        while queru.isValid():
            self.login.append(queru.value('login'))
            self.psw.append(queru.value('password'))
            queru.next()
    
        
    def pushButton_click(self):
        print(self.login)
        print(self.psw)
        for l in range(len(self.login)):
            for p in range (len(self.psw)):
                if self.lineEdit_login.text()== self.login[l] and self.lineEdit_pasvord.text()==self.psw[p] and l== p :
                   
                    print("YES")
                else:
                    print("NO")    

    # def pushButton_click(self):
    #     q = QSqlQuery()
    #     sql_select_admin = "select * from public.test where login='admin"
      
    #     q.exec(sql_select_admin)
    #     q.first()

    #     test2_admin=[]
        

    #     while q.isValid():
    #         test2_admin.append(q.value('login'))
    #         q.next()

    #         print(test2_admin[0])
    #         self.label_2.setText(test2_admin[0])

    # def pushButton_click(self):
    #     pass


    def pushButton_click2(self):
        pass
        
    def pushButton_click3(self):
        exit()


def main():
    app=QApplication(sys.argv)
    window =Auth()
    window.show()
    app.exec()

if __name__=='__main__':
    main()
    