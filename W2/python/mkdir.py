import os
import shutil
from find_name import *

def mkdir(name_list,path):
    for filename in name_list:
        pathi=path+"/"+filename
        folder = os.path.exists(pathi)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(pathi)  # makedirs 创建文件时如果路径不存在会创建这个路径
        else:
            print("directory exists")

def find_file(path,name):
    file_list=[]
    for filename in os.listdir(path):
        if filename.find(name[2:])>=0 and len(name)!=len(filename):
            file_list.append(filename)
    return  file_list

def mv(srcfile,target_dir):                       # 移动函数
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)                       # 创建路径
        shutil.move(srcfile, target_dir + fname)          # 移动文件
        print ("move %s -> %s"%(srcfile, target_dir + fname))

def mkdir_and_mv(root):
    name_list = find_name(root)
    mkdir(name_list, root)
    for patient in name_list:
        file_list=find_file(root,patient)
        for filename in file_list:
            pathi=root+"/"+filename
            diri=root+"/"+patient+"/"
            mv(srcfile=pathi,target_dir=diri)



if __name__ == '__main__':
    mkdir_and_mv("D:/test/ST_all/29ntw7sh4r-4")

