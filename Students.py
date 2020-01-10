#!/usr/bin/env python3
n = int(input("please input number of students:"))
#建立一个存储数据的字典变量
data = {}
subjects = ('Physics','Math','History') #所有科目的列表
for i in range(0,n):
    name = input("please input name of student {}:".format(i+1)) #输入第i+1个同学的名字
    marks = []
    for x in subjects:
        marks.append(int(input("Enter marks of {}: ".format(x))))
    data[name] = marks
for x,y in data.items():
    total = sum(y)
    print("{}\'s total marks {}".format(x,total))
    if total < 120:
        print(x,"failed :\(")
    else:
        print(x,"passed :\)")
