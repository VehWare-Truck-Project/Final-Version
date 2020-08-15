import cv2
import numpy as np

class ROI:

    def __init__(self):
        # Hand written area for roi
        x_left = 65
        x_right = 1165
        y_top = 200
        y_bottom = 600
        self.vertex_x = x_right - x_left
        self.vertex_y = y_bottom - y_top
        self.vertices = np.array([[x_left, y_bottom], [x_left, y_top], [x_right, y_top], [x_right, y_bottom]], np.int32)

####################
    # When only roi is used the color of the frame changes because of the bitwise_and
    # With the bitwise_or in the rev_roi (reverse roi) the color is restored.
###################

    def roi(self, img):
        # blank mask:
        mask = np.zeros_like(img)
        # fill the mask with 255 only inside the vertices
        # outside the vertices the mask is filled with 0
        cv2.fillPoly(mask, [self.vertices], 255)
        # returning the image only where mask pixels are nonzero
        # because outside of vertices were 0 in mask after bitwise and everything except inside vertices becomes 0
        # in RGB 0 is black. Also in frame these parts always 0 so opticalflow cannot detect anything out side the
        # vertices which is the aim of ROI -region of interest
        masked = cv2.bitwise_and(img, mask)
        return masked

    def rev_roi(self, img, frame):
        # re-combine original image to roi
        # when we bitwise_or x with 0 we will have x so rest of the frame is restored.
        masked = cv2.bitwise_or(img, frame)
        return masked

    '''def run(self):
        optf = opticalF()
        while True:
            _, image_frame = self.cam.read()
            self.moveCntr = 0
            self.xCntr = 0
            self.yCntr = 0
            # This will take the wanted area, rest of the frame is black so it will not be processed by opticalflow
            new_frame = self.roi(image_frame)
            # lk_track - optical flow
            frame_gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
            vis = new_frame.copy()

            # creating empty circled image for clustering
            cul = np.zeros((1111, 301))

            # the cluster obj is created
            obj = Cluster(vis,cul)

            frame, obj = optf.detect(frame_gray, vis, obj)
            #new_frame = self.draw_big_circle(frame)
            frame,self.tupleTup = obj.cluster()

            # re-put rest of the frame with roi
            rev_new_frame = self.rev_roi(frame, image_frame)
            # draw the area
            cv2.polylines(rev_new_frame, [self.vertices], True, (0, 255, 255), 3)
            #a = np.array([[10, 110], [10, 10], [110, 10], [110, 110]], np.int32)
            #cv2.polylines(frame,[a] , True, (0, 255, 255), 3)

            cv2.imshow("Sketcher ROI", rev_new_frame)
            if cv2.waitKey(1) == 13:
                break'''
