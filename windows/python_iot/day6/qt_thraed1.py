import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
form_class = uic.loadUiType('./day6/ui/thread_ui1.ui')[0]

#메인 윈도우 클래스
class WindowClass(QMainWindow, form_class) :
    #초기화
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #btnStart를 클릭하면 procCount 시작
        self.btnStart.clicked.connect(self.procCount) 
        
        self.show()

    # 시작버튼을 눌렀을 때 실행되는 메서드
    def procCount(self):
      self.pgbTask.setRange(0, 99999) # 99 ~ 99999 까지 변경
      for i in range(0, 100000): # 100 ~ 100000 까지 변경
            print(f"출력 : {str(i)}")
            self.pgbTask.setValue(i) #pgbTask bar 진행률 올리기
            self.txbLog.append("출력 : "+str(i)) #text browser 문자열 추가하기

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWin = WindowClass()
    app.exec_()