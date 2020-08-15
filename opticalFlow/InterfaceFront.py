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
        self.setFixedSize(900, 800) #1000 800
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.label = QLabel(self)

        self.label.setPixmap(QPixmap('truck_black_front.png'))  # find how to resize

        self.label.setGeometry(380, 500, 800, 400) #800,400 #width,height
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
            rect = QRect(i[0]+75, i[1]+100, 50,100)  # 850,280,100,50 #(int x, int y, int width, int height)
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

        painter.drawRect(460, 635, 100, 165)  # sagalt 530, 635, 100, 165

        painter.drawRect(300, 635, 100, 165)  # solalt 370, 635, 100, 165

        painter.drawRect(300,535, 130, 96)  # ustsol 370,535, 130, 96

        painter.drawRect(435, 535, 130, 96)  # ustsag 505, 535, 130, 96

        qp = QPainter(self)
        for rect in self.rectObjArray:
            if(rect.x()<=565 and rect.x()>=170 and rect.y()<=735 and rect.y()>=535 ):
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
    w.resize(640, 480) #640 480
    w.show()
    sys.exit(App.exec_())