import sys
from PyQt5.QtWidgets import *
import vxod
from bd import Airport
from PyQt5.QtCore import *




class Vxod2(vxod.Vxod):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.timer = QTimer()
        self.count = 3
        self.timer.start()
        self.timer.timeout.connect(self.timer_tick)

    def timer_tick(self):
        
        self.timer.start(1000)
        self.count -=1
        # self.label_Time.setText(str(self.count))
        
        if  self.count == 0:
            self.timer.stop()
            self.count =4
            # self.lineEdit_kapcha.setDisabled(False)
            self.sw = Airport()
            self.sw.show()
            exe.close()

    

app = QApplication(sys.argv)
exe = Vxod2()
exe.show()
app.exec()