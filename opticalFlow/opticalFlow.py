from __future__ import print_function

import cv2
import numpy as np

from common import draw_str
from DBC import Cluster

lk_params = dict( winSize  = (15, 15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

feature_params = dict( maxCorners = 500,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )
class opticalF:
    def __init__(self):
        self.track_len = 10
        self.detect_interval = 5
        self.tracks = []
        self.frame_idx = 0
        self.moveCntr = 0
        self.xCntr = 0
        self.yCntr = 0

    def detect(self, frame_gray, vis, obj):

        if len(self.tracks) > 0:
            img0, img1 = self.prev_gray, frame_gray
            p0 = np.float32([tr[-1] for tr in self.tracks]).reshape(-1, 1, 2)
            p1, _st, _err = cv2.calcOpticalFlowPyrLK(img0, img1, p0, None, **lk_params)
            p0r, _st, _err = cv2.calcOpticalFlowPyrLK(img1, img0, p1, None, **lk_params)

            # first we get the absolute value of the p0-p0r
            # The reshape() function is used to give a new shape to an array without changing its data.
            # ->numpy.reshape(array, newshape, order='C')
            # and span the newly shaped array from reverse
            # this line substracts the frames from each other and gets the absolute value of it
            # then reshape the frame as a line and get the minimum changed value ?
            d = abs(p0 - p0r).reshape(-1, 2).max(-1)

            # if d is smaller than 1 the good variable will be true
            # d<1 means that there was not significant movement
            good = d < 0.1
            new_tracks = []

            for tr, (x, y), good_flag in zip(self.tracks, p1.reshape(-1, 2), good):
                # if the flag is not good this means nothing changed between two frames
                if not good_flag:
                    continue
                tr.append((x, y))
                if len(tr) > self.track_len:
                    del tr[0]
                new_tracks.append(tr)
                # draws the green dots on the video
                cv2.circle(vis, (x, y), 2, (0, 255, 0), -1)
                # filling empty circled image for clustering

                if not (x-100>1051 or x-100<0 or y-200>301 or y-200<0):
                    #print(x - 100, y - 200)
                    obj.cul[int(x-100)][int(y-200)] = 1


            self.tracks = new_tracks
            # from original code draws green lines in the area of that detected a motion
            # cv.polylines(vis, [np.int32(tr) for tr in self.tracks], False, (0, 255, 0))
            draw_str(vis, (20, 20), 'track count: %d' % len(self.tracks))

        # the code starts from here when it worked for the first time
        # the frame_idx is zero and detect_interval is always 5
        # so every 5 iteration of the code it detects the moving objects
        if self.frame_idx % self.detect_interval == 0:
            # np.zeros_like() -> Return an array of zeros with the same shape and type as a given array.
            mask = np.zeros_like(frame_gray)
            # fill array with 255 and create a white frame (RGB rules)
            mask[:] = 255
            for x, y in [np.int32(tr[-1]) for tr in self.tracks]:
                cv2.circle(mask, (x, y), 10, 0, -1)
            # goodFeaturesToTrack -> function finds the most prominent corners in the specified image region
            p = cv2.goodFeaturesToTrack(frame_gray, mask=mask, **feature_params)
            if p is not None:
                for x, y in np.float32(p).reshape(-1, 2):
                    self.tracks.append([(x, y)])

        self.frame_idx += 1
        self.prev_gray = frame_gray

        # the function for clustering is called
        obj.clusterRun()

        return vis, obj