import os
os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2,40).__str__()
import cv2
import pandas as pd

if __name__ == '__main__':
    img=cv2.imread("D:/test/cv1_3/2021-11-15/1.jpg",cv2.IMREAD_COLOR)#不要有中文路径
    f=open("D:/test/cv1_3/2021-11-15/spots_BC23209_C1(1).csv")
    data = pd.read_csv(f)
    x=data.loc[:,'X']
    y=data.loc[:,'Y']
    text=data.iloc[:,0]
    dx=50
    dy=50
    for i in range(len(x)):
        img=cv2.rectangle(img, (int(x[i]-dx), int(y[i])-dy),(int(x[i])+dx, int(y[i])+dy), (0, 0, 255), 5,4)#BGR, not RGB
        img=cv2.putText(img,str(text[i]),(int(x[i]-dx*4/5),int(y[i]+dy/2)),cv2.FONT_HERSHEY_COMPLEX ,0.8, (0,0,255), 1)
    cv2.imwrite("D:/test/cv1_3/2021-11-15/result.jpg",img)
    f.close()