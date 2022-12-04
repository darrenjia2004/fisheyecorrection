import cv2
import numpy as np
import os
import glob
import sys
import math

def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

# You should replace these 3 lines with the output in calibration step

#ImageSet1
# DIM=(4000, 3000)
# K=np.array([[1747.2440401766007, 0.0, 1976.9937411207925], [0.0, 1747.3591267557758, 1504.4953960401783], [0.0, 0.0, 1.0]])
# D=np.array([[0.04817021678815688], [0.005989257257503963], [0.03676882461321512], [-0.03295647420798284]])
# cx = 1976.9937411207925
# cy = 1504.4953960401783

#ImageSet2
# DIM=(4000, 3000)
# K=np.array([[1755.6316698068365, 0.0, 1980.1953760206702], [0.0, 1753.5289071835912, 1509.5886452520122], [0.0, 0.0, 1.0]])
# D=np.array([[0.041996226428033634], [-0.0016690714423546373], [0.06586625639887955], [-0.054561544133844495]])
# cx = 1980.1953760206702
# cy = 1509.5886452520122

#iphone
DIM=(4032, 3024)
K=np.array([[1631.0932475943891, 0.0, 2012.802558311828], [0.0, 1627.1020529750974, 1514.6936663992676], [0.0, 0.0, 1.0]])
D=np.array([[0.24954264915609106], [0.46601668217308473], [-0.7252897077248179], [0.622186283030176]])
cx=2012.802558311828
cy=1514.6936663992676
width=4032
height=3024

def undistort(img_path):
    img = cv2.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    resize = ResizeWithAspectRatio(undistorted_img, width=1280)
    #cv2.imwrite('./AFOV/bricks.jpg',resize)
    cv2.imshow("undistorted", resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    undistortedpoints = cv2.undistortPoints(np.float32([[cx,cy], [-0.5,cy], [width+.5, cy], [cx, height+.5], [cx, -0.5]]).reshape((-1, 1, 2)), K, D)
    print(undistortedpoints)
    print(angle([2.6319310e-02,  7.3012626e-01, 1], [  6.4821027e-02 ,-1.0349880e+00, 1]))
    # images = glob.glob('*.jpg')
    # for image in images:
    #     undistort(image)
