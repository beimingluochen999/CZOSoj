num=int(input())   #输入

temp=0 #定义变量，用于累积后续循环中的数据
for i in range(1,num+1):  #从1到num（注意：range区间左闭右开）
    temp+=i  #将当前数据累加到变量中

print(temp)  #输出

#一行代码实现法(新手不推荐)：print(sum(list(range(1,int(input())))))
