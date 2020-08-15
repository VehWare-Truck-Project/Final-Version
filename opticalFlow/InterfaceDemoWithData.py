#asil calisan kod
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QRect, QPoint, QTimer



class Example(QWidget):
    def __init__(self,vertex_x,vertex_y):
        super(Example, self).__init__()

        self.title = "Truck Interface"

        self.top = 150

        self.left = 150

        self.width = 1000

        self.height = 800

        self.flag=200

        self.centerX=0

        self.centerY=0

        self.ratio_x=vertex_x

        self.ratio_y=vertex_y # su anda kullanilmiyo

        self.initUI()

        self.rectObjArray=[]

    def initUI(self):
        self.setFixedSize(1000, 800)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.label = QLabel(self)

        self.label.setPixmap(QPixmap('truck_black.png'))  # find how to resize

        self.label.setGeometry(250, 200, 800, 400) #800,400 #width,height
        print(self.label.width())
        #self.rect = QRect()

        #self.onPaint() program her basladiginda car olmayabilir

        self.hlayout = QHBoxLayout(self)
        self.hlayout.addStretch(1)
        self.show()

    def delRectObj(self):

         self.rectObjArray.clear()

    def createRectObj(self,tupleArray):

        for i in tupleArray:
            if i[0]==-1 or i[1]==-1:
                continue
            rect = QRect(i[0], i[1], 100,50)  # 850,280,100,50 #(int x, int y, int width, int height)
            self.rectObjArray.append(rect)
        self.update()

    def onPaint(self):

        self.rect = QRect(self.centerX-50, self.centerY-25, 100, 50) #850,280,100,50 #(int x, int y, int width, int height)
        self.update()

    def onMove(self,cX,cY,priorCX, priorCY):

        newCX=float(480*cX)/self.ratio_x
        newPriorCx= float(480*priorCX)/self.ratio_x

        if not self.rect.isNull():
            self.rect.translate(QPoint(newCX-newPriorCx, cY-priorCY))
            self.update()
            self.show()

    def setCenterX(self,data):

        self.centerX=data
        #print('x', self.centerX)



    def setCenterY(self, data):

        self.centerX = data
        #print('y', self.centerY)


    def paintEvent(self, event): #change the opacity of regions

        painter = QPainter(self)

        painter.setPen(QPen(Qt.black,  3, Qt.DashLine))

        painter.setBrush(QBrush(QColor.fromRgb(0,255,0,100), Qt.SolidPattern)) #fromRgb(int r, int g, int b, int a = 255) a=alpha-chanel->transperancy

        painter.drawRect(200, 280, 70, 120) #soldikust #1100 #480

        painter.drawRect(200, 404, 70, 120) #soldikalt

        painter.drawRect(275, 280, 130, 60) #yanust1

        painter.drawRect(410, 280, 130, 60) #yanust2

        painter.drawRect(545, 280, 130, 60) #yanust3

        painter.drawRect(680, 280, 70, 120) #sagdikust

        painter.drawRect(680, 404, 70, 120) #sagdikalt

        painter.drawRect(275, 460, 130, 63)  # yanalt1

        painter.drawRect(410, 460, 130, 63)  # yanalt2

        painter.drawRect(545, 460, 130, 63)  # yanalt3

        qp = QPainter(self)
        for rect in self.rectObjArray:
            if(rect.x()<=750 and rect.x()>=130 and rect.y()<=550 and rect.y()>=270 ):
                qp.setPen(QPen(Qt.black,  3, Qt.DashLine))
                qp.setBrush(QColor(200, 0, 0))
                qp.drawRect(rect)
            else:
                qp.setPen(QPen(Qt.black,  3, Qt.DashLine))
                qp.setBrush(QBrush(QColor.fromRgb(0,255,0), Qt.SolidPattern))
                qp.drawRect(rect)



if __name__ == '__main__':
    import sys

    App = QApplication(sys.argv)
    w = Example()
    w.resize(640, 480)
    w.show()
    sys.exit(App.exec_())