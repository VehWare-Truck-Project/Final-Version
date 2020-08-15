
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QRect, QPoint, QTimer
import cv2
import numpy as np




class Example(QWidget):
    def __init__(self,vertex_x,vertex_y): #takes dimensions of the demo video
        super(Example, self).__init__()

        self.title = "Truck Front User Interface"

        self.top = 150

        self.left = 150

        self.width = 1000

        self.height = 800

        self.flag=200

        self.centerX=0

        self.centerY=0

        self.ratio_x=vertex_x # su anda kullanilmiyo

        self.ratio_y=vertex_y # su anda kullanilmiyo

        self.initUI()

        self.rectObjArray=[]

    def initUI(self):
        self.setFixedSize(900, 800) #sets the window size
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.label = QLabel(self) #creates a label for the truck image

        self.label.setPixmap(QPixmap('truck_black_front.png'))

        self.label.setGeometry(380, 500, 800, 400)

        self.hlayout = QHBoxLayout(self)
        self.hlayout.addStretch(1)
        self.show()

    def delRectObj(self): #deletes the car object

         self.rectObjArray.clear() #koordinatlarin bulundugu array i temizler

    def createRectObj(self,tupleArray): # creates a car object

        for i in tupleArray: #tuple contains -1 if algorithm couldnt detect car
            if i[0]==-1 or i[1]==-1:
                continue # continue without creating object if there is no detection
            rect = QRect(i[0]+75, i[1]+100, 50,100)   #(int x, int y, int width, int height) creates car object
            self.rectObjArray.append(rect) #add the created objcet to an array
        self.update()

    def onPaint(self): #kullanilmiyo

        self.rect = QRect(self.centerX-50, self.centerY-25, 100, 50) #850,280,100,50 #(int x, int y, int width, int height)
        self.update()

    def onMove(self,cX,cY,priorCX, priorCY): #kullanilmiyo

        newCX=float(480*cX)/self.ratio_x
        newPriorCx= float(480*priorCX)/self.ratio_x

        if not self.rect.isNull():
            self.rect.translate(QPoint(newCX-newPriorCx, cY-priorCY))
            self.update()
            self.show()

    def setCenterX(self,data): #kullanilmiyo

        self.centerX=data
        #print('x', self.centerX)



    def setCenterY(self, data): #kullanilmiyo

        self.centerX = data
        #print('y', self.centerY)


    def paintEvent(self, event): #draws the regions around the truck and change their colors green to red if there is any car in the region

        painter = QPainter(self)

        painter.setPen(QPen(Qt.black,  3, Qt.DashLine))

        painter.setBrush(QBrush(QColor.fromRgb(0,255,0,100), Qt.SolidPattern)) #fromRgb(int r, int g, int b, int a = 255) a=alpha-chanel->transperancy

        painter.drawRect(460, 635, 100, 165)  # sagalt 530, 635, 100, 165

        painter.drawRect(300, 635, 100, 165)  # solalt 370, 635, 100, 165

        painter.drawRect(300,535, 130, 96)  # ustsol 370,535, 130, 96

        painter.drawRect(435, 535, 130, 96)  # ustsag 505, 535, 130, 96

        qp = QPainter(self) #change colors
        for rect in self.rectObjArray:
            if(rect.x()<=565 and rect.x()>=170 and rect.y()<=735 and rect.y()>=535 ):
                qp.setPen(QPen(Qt.black,  3, Qt.DashLine))
                qp.setBrush(QColor(200, 0, 0))
                qp.drawRect(rect)
            else:
                qp.setPen(QPen(Qt.black,  3, Qt.DashLine))
                qp.setBrush(QBrush(QColor.fromRgb(0,255,0), Qt.SolidPattern))
                qp.drawRect(rect)



def main():
    App = QApplication(sys.argv)
    w = Example(ROIClass.vertex_x, ROIClass.vertex_y)  # you create with the parameters of your demo video/like this
    w.resize(640, 480)
    w.show()

    while True:  # burda frameleri dondugun bir loop olmali
        w.delRectObj()  # burda her bir frame de car objesini silmelisin

        # TODO: burda algoritmani frame frame calisitirmalisin
        # TODO: burda algoritmandan elde ettigin koordinatlari bir arrayin icinde tupple lar halinde (yani x ve y) tutmalisin

        w.createRectObj(tupleArray)  # sonra elde ettigin arrayi bunun icine yollamalisin

    sys.exit(App.exec_())


if __name__ == '__main__':
    import sys
    main()
    cv2.destroyAllWindows()