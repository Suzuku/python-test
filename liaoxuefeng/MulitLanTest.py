# 用户输入文件名，脚本遍历当前路径下的所有文件夹和文件，匹配到包含该文件名的所有文件，并添加到json文件中
import os
import json

# By Kiri
# 使用绝对路径 先把json文件内容读取 然后赋值 再写入  缺点：无序，而且会覆盖同名属性


def appendJSON(dir, jsonDict):
    with open(dir, 'r', encoding='utf-8') as f:
        content = f.read()
        # 清除JSON的BOM
        if content.startswith(u'\ufeff'):
            content = content.encode('utf8')[3:].decode('utf8')
        content_str = json.loads(content)
    for i in content_str:
        jsonDict[i] = content_str[i]
    with open(dir, 'w', encoding='utf-8') as f:
        json.dump(jsonDict, f, indent=4, ensure_ascii=False)

# 第一次遍历当前目录  （使用os.walk()可以优化）当时对着几个原生库方法自己撸出来的，适用性和优化做的太差了。好绕


def printStrFile(arg):
    main_dir = [x for x in os.listdir('.')]
    file_list = [x for x in main_dir if os.path.isfile(x)]
    dir_list = [x for x in main_dir if os.path.isdir(x)]
    for x in file_list:
        if(arg in x):
            result_list.append(os.path.abspath(x))
    # 开始
    recursion_list(dir_list, arg, result_list)
    # 输出结果List
    if result_list == []:
        print('No Match')
    else:                             
        for x in result_list:
            print(x)
            appendJSON(x, dict)


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
# 需要追加的字符串在这里定义  会覆盖已有属性
dict = {"input233": "输入口",
        "ioInput233": "IO输入口",
        "function233": "用途",
        "output233": "输出口",
        "ioOutput233": "IO输出口",
        "disable233": "禁用",
        "custom233": "自定义",
        "openDoor233": "开门按钮",
        "doorStatus233": "门状态"
        }
# 用户输入想要批量处理的文件名
match_str = input(
    'Please enter a String to match the file in this DIR  \n')
printStrFile(match_str)
