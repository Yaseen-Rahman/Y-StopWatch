from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QMenu
from PyQt5.QtCore import Qt,QTimer,QTime
import sys
from PyQt5.QtGui import QIcon

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.timer = QTimer()
        self.timer_label = QLabel("00:00:00.00",self)
        self.data = QLabel("By Yaseen(Y-Softwares)",self)
        self.setWindowIcon(QIcon("stop_icon.ico"))
        self.start_button = QPushButton("Start",self)
        self.stop_button = QPushButton("Stop",self)
        self.reset_button = QPushButton("Reset",self)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.setWindowTitle("Stopwatch")
        self.setGeometry(300,400,300,200)
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addWidget(self.timer_label)
        vbox.addWidget(self.data)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.start_button.setObjectName("start_button")
        self.stop_button.setObjectName("stop_button")
        self.reset_button.setObjectName("reset_button")
        self.data.setObjectName("data")  
        self.timer_label.setObjectName("time")
        self.data.setAlignment(Qt.AlignCenter)      
        self.setStyleSheet("""
        QPushButton{
        font-size: 50px;
        font-family: calibri;
        border: 1px solid;
        border-radius: 10px;
        font-weight: bold;
        padding: 15px;
        color: hsl(0,0,87);}
        QLabel#time{
        font-size: 100px;
        font-family: calibri;
        font-weight: bold;
        background-color: lightblue;
        }
        QPushButton#start_button:hover{
        color: hsl(100,250,95);
        }
        QPushButton#stop_button:hover{
        color: hsl(100,250,95);
        }
        QPushButton#reset_button:hover{
        color: hsl(100,250,95);
        }
        QPushButton#start_button:pressed{
        color: red;
        }
        QPushButton#stop_button:pressed{
        color: red;
        }
        QPushButton#reset_button:pressed{
        color: red;
        }
        """)
        self.timer.timeout.connect(self.update_time)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

    def start(self):
        self.timer.start(10)


    def stop(self):
        self.timer.stop()


    def reset(self):
        self.time = QTime(0,0,0,0)
        self.timer_label.setText(self.format_time(self.time))


    def format_time(self,time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
    
    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.timer_label.setText(self.format_time(self.time))

def main():
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    app.exit(app.exec_())

if __name__ == "__main__":
    main()