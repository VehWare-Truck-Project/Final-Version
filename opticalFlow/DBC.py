
import numpy as np
import cv2

class Cluster:
    def __init__(self, image, cluster):
        self.img = image
        self.cul = cluster
        self.minPoints = 5
        self.maxCuli = 3
        self.maxCulj = 1
        self.rani = len(self.cul)
        self.ranj = len(self.cul[1])
        self.stepSize = 100 #max distance
        # if the array's element is 1 it means pixel is moving, 2 means the moving pixels are more than minPoints
        # in stepSize, 3 means segment is a part of a cluster, 4 means segment is the center of the cluster

    def getXY(self):
        tupleArray = []
        flag =0
        for i in range(0, self.rani, self.stepSize):
            for j in range(0, self.ranj, self.stepSize):
                if self.cul[i][j] == 4:
                    cv2.circle(self.img, (int(i + 65), int(j + 200)), 50, (255, 255, 0), 5)
                    tupleTup = (int(i + 65), int(j + 200))
                    tupleArray.append(tupleTup)
                    flag = 1
                    #print(int(i + 65), int(j + 200))
                '''if self.cul[i][j] == 2:
                    cv2.circle(self.img, (int(i + 65), int(j + 200)), 50, (255, 0, 0), 5)
                    tupleTup = (int(i + 65), int(j + 200))
                    # print("p")'''
        if not flag:
            tupleArray.append((-1, -1))
        return self.img, tupleArray

    def cluster(self):
        for i in range(0, self.rani, self.stepSize):
            for j in range(0, self.ranj, self.stepSize):
                if self.cul[i][j] == 2:
                    sumci = 0
                    sumcj = 0
                    count = 0

                    if i < self.stepSize * self.maxCuli:
                        begini = i
                    else:
                        begini = i - self.stepSize * self.maxCuli

                    if j < self.stepSize * self.maxCulj:
                        beginj = j
                    else:
                        beginj = j - self.stepSize * self.maxCulj

                    if i + self.stepSize * self.maxCuli > self.rani:
                        endi = self.rani
                    else:
                        endi = i + self.stepSize * self.maxCuli

                    if j + self.stepSize * self.maxCulj> self.ranj:
                        endj = self.ranj
                    else:
                        endj = j + self.stepSize * self.maxCulj

                    #print(endi)
                    for ci in range(begini, endi, self.stepSize):
                        for cj in range(beginj, endj, self.stepSize):
                            if self.cul[ci][cj] == 2:
                                sumci += ci
                                sumcj += cj
                                count += 1
                                self.cul[ci][cj] = 3
                            elif self.cul[ci][cj] == 3:
                                sumci += ci
                                sumcj += cj
                                count += 1
                                #print("Elif")
                            elif self.cul[ci][cj] == 4:
                                sumci += ci
                                sumcj += cj
                                count += 1
                                self.cul[ci][cj] = 3
                    newi = int(sumci / count)
                    newj = int(sumcj / count)
                    self.cul[newi][newj] = 4
                    '''counti = 1
                    countj = 1
                    previ = i
                    prevj = j
                    while i <= self.rani and self.cul[i][j] == 2:
                        counti += 1
                        self.cul[i][j] = 3
                        i +=self.stepSize
                        while j <= self.ranj and self.cul[i][j] == 2:
                            countj += 1
                            self.cul[i][j] = 3
                            j +=self.stepSize
                        j = prevj
                    newi = int(counti/2)*self.stepSize
                    newj = int(countj/2)*self.stepSize
                    i = previ
                    j = prevj
                    self.cul[i + newi][j+newj] = 4'''

    def clusterRun(self):
        for i in range(0, self.rani, self.stepSize):
            for j in range(0, self.ranj, self.stepSize):

                count = np.count_nonzero(self.cul[i:i+self.stepSize,j:j+self.stepSize] == 1 )
                #print(count)
                if count > self.minPoints:
                    self.cul[i][j] = 2
                    #declares that this segment of the array has a cluster
        self.cluster()