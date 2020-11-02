# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出绝对路径。
import os


def printStrFile(arg):
    main_dir = [x for x in os.listdir('.')]
    file_list = [x for x in main_dir if os.path.isfile(x)]
    dir_list = [x for x in main_dir if os.path.isdir(x)]
    for x in file_list:
        if(arg in x):
            result_list.append(os.path.abspath(x))
    # 开始
    recursion_list(dir_list, arg, result_list)
    # 输出结果
    if result_list == []:
        print('No Match (*^▽^*)')
    else:
        for x in result_list:
            print(x)


# 递归遍历目录,传参分别为只含目录的列表，比对字符串，结果list，和上一级的path
def recursion_list(Dir__List, arg, mainList, fatherPath=''):
    # List是目录的集合
    if Dir__List == []:
        return
    for item in Dir__List:
        # 如果是第一次递归 则没有父亲路径
        if fatherPath:
            # 当前目录的绝对路径
            dir_path = os.path.join(fatherPath, item)
        else:
            dir_path = os.path.abspath(item)
        file_list = [x for x in os.listdir(
            dir_path) if os.path.isfile(os.path.join(dir_path, x))]
        dir_list = [x for x in os.listdir(
            dir_path) if os.path.isdir(os.path.join(dir_path, x))]
        for x in file_list:
            if(arg in x):
                mainList.append(os.path.abspath(os.path.join(dir_path, x)))
        # 获取到当前目录下的目录文件列表，开始下一次递归
        recursion_list(dir_list, arg, result_list, os.path.abspath(item))


result_list = []
match_str = input('Please enter a String to match the file in this DIR ヽ(￣▽￣)ﾉ \n')
printStrFile(match_str)
