from __future__ import print_function

import cv2
import numpy as np

from opticalFlow import opticalF
import video
from DBC import Cluster

from roi import ROI
#from InterfaceDemoWithData import Example
from InterfaceFront import Example

from PyQt5.QtWidgets import QApplication


class Demo:
    def __init__(self, video_src):
        self.cam = video.create_capture(video_src)

    def run(self):
        optf = opticalF()

        counter = 0
        previousTuple = ()
        carCount = 0
        ROIClass = ROI()
        w = Example(ROIClass.vertex_x, ROIClass.vertex_y)
        w.resize(640, 480)
        w.show()
        while True:
            w.delRectObj()
            ############################################################ROI
            _, image_frame = self.cam.read()
            # This will take the wanted area, rest of the frame is black so it will not be processed by opticalflow
            new_frame = ROIClass.roi(image_frame)
            # lk_track - optical flow
            frame_gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
            vis = new_frame.copy()

            # creating empty circled image for clustering
            cul = np.zeros((ROIClass.vertex_x + 1, ROIClass.vertex_y + 1))

            # the cluster obj is created
            obj = Cluster(vis, cul)

            frame, obj = optf.detect(frame_gray, vis, obj)

            ############################################################ROI END UI BEGIN
            # tupleTup x, y tuple i
            frame, tupleArray = obj.getXY()

            #carCount = len(tupleArray)

            w.createRectObj(tupleArray)


            ############################################################UI END ROI BEGIN
            # re-put rest of the frame with roi
            rev_new_frame = ROIClass.rev_roi(frame, image_frame)
            # draw the area
            cv2.polylines(rev_new_frame, [ROIClass.vertices], True, (0, 255, 255), 3)

            cv2.imshow("Sketcher ROI", rev_new_frame)

            if cv2.waitKey(1) == 13:
                break
            ############################################################ROI END


def main():
    import sys
    try:
        video_src = sys.argv[1]
    except:
        video_src = 0

    App = QApplication(sys.argv)
    Demo(video_src).run()
    print('Done')


if __name__ == '__main__':
    print(__doc__)
    main()
    cv2.destroyAllWindows()
