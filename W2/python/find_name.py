import os

def find_name(path):
    # get name
    name_list = []
    for filename in os.listdir(path):
        if filename.find("jpg") >= 0:
            tmp_list = list(filename)
            length = len(tmp_list)
            cut = 0
            for i in range(length):
                if tmp_list[length - i - 1] == '_':
                    cut = length - i - 1
                    break
            tmp_str = filename[3:cut]
            name_list.append(tmp_str)
    tmp_set = set(name_list)
    name_list = list(tmp_set)
    return name_list

if __name__ == '__main__':
    print(find_name("D:/test/ST_all/29ntw7sh4r-4"))


