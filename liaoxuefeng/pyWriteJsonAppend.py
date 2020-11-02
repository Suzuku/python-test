import json

# 追加指定字符串 会覆盖已有属性
dict = {"input": "输入口",
        "ioInput": "IO输入口",
        "function": "用途",
        "output": "输出口",
        "ioOutput": "IO输出口",
        "disable": "禁用",
        "custom": "自定义",
        "openDoor": "开门按钮",
        "doorStatus": "门状态"}


def appendJSON(dir, jsonDict):
    with open(dir, 'r', encoding='utf-8') as f:
        load_str = json.load(f)
    for i in load_str:
        jsonDict[i] = load_str[i]
    with open(dir, 'w', encoding='utf-8') as f:
        json.dump(jsonDict, f, indent=4, ensure_ascii=False)


appendJSON('D:\Code-test\python\pytest.json', dict)
