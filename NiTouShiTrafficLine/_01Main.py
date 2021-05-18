# coding=utf-8
import numpy as np
import cv2

# 拓哥牛逼

np.set_printoptions(suppress=True, precision=4)

H = np.array([[-0.51050696, -2.11815651, 642.48018518],
              [0.00253205, 0.04427529, -167.26350596],
              [-0.00008633, -0.00427193, 1.]])

# 相机参数
Dist = np.array([-0.37959,   0.20457,   0.00046,   -0.00029,  0.00000 ], dtype=np.float32)
K = np.array([[315.51468, 0, 326.07501],
              [0, 313.49477, 222.20442],
              [0, 0, 1]], dtype=np.float32)

Frame = 0
Video = cv2.VideoCapture('./line20191123_2.avi')
Video.set(1, Frame)

while 1:
    ret, Img = Video.read()
    if ret == True:
        Frame = Frame + 1
        UndistImg = cv2.undistort(Img, K, Dist)
        WarpedImg = cv2.warpPerspective(UndistImg, H, (1000, 1000))
        cv2.imshow('Video', WarpedImg)
        key = cv2.waitKey(5)
        if key != -1:
            exit()
    else:
        break
print('End')
Video.release()

