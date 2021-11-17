import os
os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2,40).__str__()
import cv2


origin=cv2.imread("E:/academics/project/W1/data/GSM/GSM3036911_PDAC-A-ST1-HE.jpg",cv2.IMREAD_COLOR)
img=cv2.resize(origin, (5000, 5000))
cv2.imshow('image',img)
cv2.waitKey(100000)
cv2.destroyAllWindows()


