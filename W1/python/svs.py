#reference:https://blog.csdn.net/caicai2526/article/details/75324679?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522163681402116780274141327%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=163681402116780274141327&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-75324679.first_rank_v2_pc_rank_v29&utm_term=openslide+read_region&spm=1018.2226.3001.4187
import openslide
from openslide.deepzoom import DeepZoomGenerator
import matplotlib.pyplot as plt
import numpy as np
import random

#load file
slide = openslide.open_slide(r"E:\academics\project\W1\data\divisioin\TCGA-AG-A002-01A-01-BS1.48af6e9c-1874-4294-ba2c-c2e5666ca0d0.svs")

#get the size of each clarity level of the svs picture
downsamples=slide.level_downsamples #每一个级别K的对应的下采样因子，下采样因子应该对应一个倍率
#看看最多能有多大的level/clarity
level_count = slide.level_count
print("total clarity level: "+str(level_count))

#get the size of the total size of the intact svs file
[w, h] = slide.level_dimensions[0] #最高倍下的宽高

k=1#level/clarity
#get the size of the picture we are going to show. Here k=2, which is the level of clarity
size1 = int(w*(downsamples[0]/downsamples[k]))# 计算级别k下的总宽
size2 = int(h*(downsamples[0]/downsamples[k])) # 计算k下的总高

#convert the svs to 2-dimension array
#read_region(location, level, size) 返回一个RGBA图像，包含指定区域的内容。location指0级别下左上角位置的坐标，元组，level指级别，整数，size是（width， height）是元组
#attention that here we must use (size1,size2), which is the size of 2D array,or there would be nothing
region = np.array(slide.read_region((0, 0), k, (size1, size2)))#先读取，再数组化
print(region.shape)
print(w,h)
print(size1, size2)

#cut
#attention that here x,y are reversed compared to what we think
for i in range(20):
    y=random.randint(0, size1-1000)
    x = random.randint(0, size2 - 1000)
    print(x,y)
    regionx=region[x:x+1000,y:y+1000,:]
    print(regionx.shape)
    plt.figure()
    plt.imshow(regionx)
    plt.show()


slide.close()