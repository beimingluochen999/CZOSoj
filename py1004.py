num=int(input())  #依旧输入

temp=1  #依旧变量初始化（注意：因为要累乘，所以不能初始化为0）
for i in range(1,num+1):
    temp*=i
print(temp)