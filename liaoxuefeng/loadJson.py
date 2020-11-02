import json

with open('./pytest.json','r') as f:
     load_str=json.load(f)
     print(load_str,type(load_str))

    #  {'foo': '253', 'kiri': '233'} <class 'dict'>
