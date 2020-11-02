
height = float(input('请输入你的身高（米）'))
weight = float(input('请输入你的体重（kg）'))
bmi=weight/(height*height)

if bmi<18.5:
    print('过轻')
elif 18.5<=bmi<=25:
    print('正常')
elif 25<bmi<=28:
    print('过重')
elif 28<bmi<=32:
    print('肥胖')
elif bmi>32:
    print('严重肥胖')    