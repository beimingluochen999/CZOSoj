def func(x):  #定义阶乘函数，也可以直接套入循环
    t=1
    for i in range(1,x+1):
        t=t*i
    return t

num=int(input())  #输入
temp=0  #变量初始化

for i in range(1,num+1):
    temp+=func(i)  #把累乘结果加到temp
print(temp)