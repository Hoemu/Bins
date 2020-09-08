# QdesktopWidget 可以得到和屏幕相关的类
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm,self).__init__()
        self.setWindowTitle('居中程序')
        self.resize(300,200)

    def center(self):
        #获取屏幕坐标
        screen=QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size=self.geometry()
        newLeft=(screen.width()-size.width())/2;
        newTop=(screen.height()-size.height())/2;
        self.move(newLeft,newTop)

if __name__=='__main__':
    app=QApplication(sys.argv)
    # 设置应用程序图标
    app.setWindowIcon(QIcon('E:\\Users\\hasee\\Pictures\\其他\\OIP (2).ico'))
    main=CenterForm()
    main.show()

    sys.exit(app.exec_())
