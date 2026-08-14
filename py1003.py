num=int(input())  #输入

temp=0  #初始化累计变量
for i in range(1,num+1,2):  #启用for循环，第三个值为步长，每个2步取值，保证取值为集数
    temp+=i
print(temp)

#一行代码法见py1001