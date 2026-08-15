def turn(num):   #定义函数：传入一个数，返回其回文数
    nL = list(str(num))  #转化为字符串列表
    n=""
    for i in range(len(nL) - 1, -1, -1):  #反向遍历
        n=n+nL[i]   #拼接至字符串中
    return int(n)

num=int(input())
n1=num*1  #我强迫症，所以单独剥离开来，后续的n1直接用num也可行
count=0  #计数菌

while(1):
    if n1==turn(n1):  #判断当前数是否回文
        break
    n1+=turn(n1)  #自增自己的回文数
    count+=1   #计数君上线

print(count)