import sys, cv2, os
import numpy as np
from img_view import IMG_WIN
from TRPGsurface import Ui_TRPGsurface   # Ui_TRPGsurface 是 QtDesigner 导出的 py 文件中的 object 子类
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtGui import QImage, QPixmap
import ctypes

try:
    temp=ctypes.windll.LoadLibrary( 'opencv_ffmpeg341_64.dll' )
except:
    pass

    

_translate = QtCore.QCoreApplication.translate  
image_type = ['jpg','png','jpeg']


class Demo(QWidget, Ui_TRPGsurface): # 双继承
    def __init__(self):
        super(Demo, self).__init__()
        
        self.setupUi(self) # setupUi 方法是 Ui_TRPGsurface 的类方法
        self.retranslateUi(self) # 重新加载 UI 布局的设置
        self.graphic=IMG_WIN(self.character_image)	# 实例化 IMG_WIN 类，是场景和立绘绘制的核心类
        self.character_path = os.getcwd()
        self.place_path = os.getcwd()

        # 初始化设置
        self.time = [12,0]
        self.font_size_big = 36
        self.font_size_small = 24
        self.update_path()   # 初始化人物立绘和场景背景复选栏

        # 选取目录按钮
        self.character_pathchooser.clicked.connect(self.select_character_path)
        self.place_pathchooser.clicked.connect(self.select_place_path)

        # 将日期时间类控件连接上槽函数
        self.fontsize_on.clicked.connect(lambda: self.font_change(1))
        self.fontsize_off.clicked.connect(lambda: self.font_change(0))
        self.calendar.clicked.connect(self.date_time_change)
        self.add3hour.clicked.connect(lambda: self.time_change(3,0))
        self.add1hour.clicked.connect(lambda: self.time_change(1,0))
        self.minus1hour.clicked.connect(lambda: self.time_change(-1,0))
        self.minus3hour.clicked.connect(lambda: self.time_change(-1,0))
        self.add10min.clicked.connect(lambda: self.time_change(10,1))
        self.add5min.clicked.connect(lambda: self.time_change(5,1))
        self.minus5min.clicked.connect(lambda: self.time_change(-5,1))
        self.minus10min.clicked.connect(lambda: self.time_change(-10,1))

        # 文本框高度自适应
        self.text_Browser.textChanged.connect(self.textAreaChanged);

        # 复位与应用按钮
        self.apply_button.clicked.connect(self.apply)
        self.clear_button.clicked.connect(self.clear)
   
    def select_character_path(self):
        # 选择立绘图片目录
        filePath = QFileDialog.getExistingDirectory(
            self,  # 父窗口对象
            "选择人物立绘所在目录",  # 标题
            self.character_path  # 起始目录
        )
        if filePath == '':
            return
        else:
            # self.character_path = np.fromfile(filePath, dtype=np.uint8)
            self.character_path = filePath
            self.update_path()
    
    def select_place_path(self):
        # 选择场景图片目录
        filePath = QFileDialog.getExistingDirectory(
            self,  # 父窗口对象
            "选择背景图片所在目录",  # 标题
            self.place_path  # 起始目录
        )
        if filePath == '':
            return
        else:
            # self.place_path = np.fromfile(filePath, dtype=np.uint8)
            self.place_path = filePath
            self.update_path()

    def update_path(self):
        # 获知当前立绘目录下的所有图片文件并创建为列表
        # 对场景图片也作如此操作
        self.character_combo.clear()
        self.place_combo.clear()

        c_dirs = os.listdir( self.character_path )
        p_dirs = os.listdir( self.place_path )

        self.character_name2file = dict()
        self.character_names = []
        self.place_name2file = dict()
        self.place_names = []

        for file in c_dirs:
            index = file.find('.')
            if index >= 0:
                if file[index+1:] in image_type:
                    self.character_name2file[file[:index]] = file
                    self.character_names.append(file[:index]) 
        
        for file in p_dirs:
            index = file.find('.')
            if index >= 0:
                if file[index+1:] in image_type:
                    self.place_name2file[file[:index]] = file
                    self.place_names.append(file[:index]) 

        self.character_combo.addItems(self.character_names)
        self.place_combo.addItems(self.place_names)

        self.apply()

        self.current_character = self.character_combo.currentText()
        self.current_place = self.place_combo.currentText()

    def clear(self):
        try:
            self.character_combo.setCurrentText('keeper')
            self.apply()
        except:
            print('Error! No existing \'keeper\' image.')

    def apply(self):  # 调用 IMG_WIN 类，将人物立绘和场景绘制上去
        self.current_character = self.character_combo.currentText()
        self.current_place = self.place_combo.currentText()

        cfilePath = self.character_name2file[self.current_character]
        cfilePath = self.character_path + '/' + cfilePath

        pfilePath = self.place_name2file[self.current_place]
        pfilePath = self.place_path + '/' + pfilePath

        print('path set done')

        '''
        img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
        '''

        self.pShow = QPixmap(pfilePath)
        self.cShow = QPixmap(cfilePath)

        print('image prepare done')

        self.graphic.addAll(self.pShow,self.cShow)
    
    def textAreaChanged(self):  # 文本框自动调整高度
        self.text_Browser.setFixedHeight(20)   # 先把高度设置很小，强制让滚动条出现。
        height = self.text_Browser.verticalScrollBar().maximum() - self.text_Browser.verticalScrollBar().minimum() + self.text_Browser.verticalScrollBar().pageStep()
        self.text_Browser.setFixedHeight(height)

    def time_change(self, value, flag):
        # 改变时间后触发，flag为1表示变更分钟，flag为0表示变更小时
        self.time[flag] += value
        self.time = [(self.time[0] + self.time[1]//60)%24, self.time[1]%60]
        self.date_time_change()

    def font_change(self, flag):
        # 更改字体大小，flag为1表示增大，flag为0表示减小
        self.font_size_big = self.font_size_big+ 1 if flag == 1 else self.font_size_big - 1
        self.font_size_small = self.font_size_small + 1 if flag == 1 else self.font_size_small - 1
        self.date_time_change()

    def date_time_change(self):
        # 将日期、时间的更改应用到右侧文本框
        self.date = self.calendar.selectedDate()
        time = list(map(str,self.time))
        if len(time[1]) == 1:
            time[1] = '0'+time[1]
        self.text_Browser.setHtml(_translate("TRPGsurface", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n" +
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:{ysize}pt;\">{} 年</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:{fsize}pt; font-weight:600;\">{} 月 {} 日</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:{fsize}pt; font-weight:600;\">{} </span><span style=\" font-size:{fsize}pt; font-weight:600; color:#0011ff;\">{}:{}</span><span style=\" font-size:36pt; font-weight:600;\"> </span></p></body></html>".format(
    self.date.year(),self.date.month(),self.date.day(),self.date.toString('ddd'),time[0],time[1],fsize = self.font_size_big,ysize = self.font_size_small)))
        
       


if __name__ == '__main__':
    

    app = QApplication(sys.argv[1:])
    
    #获取显示器分辨率大小
    desktop = QApplication.desktop()
    screenRect = desktop.screenGeometry()
    h = screenRect.height()
    w = screenRect.width()

    demo = Demo()
    demo.resize(w/2, h)
    demo.move(w/2,0)
    demo.show()
    demo.date_time_change()
    demo.apply()
    sys.exit(app.exec_ ())