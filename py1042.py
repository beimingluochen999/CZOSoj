num=int(input())

numList=[num//100,num%100//10,num%10]  #拆分个十百位数字【百，十，个】
numList.sort(reverse=True)  #把数字列表降幂排序
for i in numList:
    print(i,end="")  #循环输出，end保证不换行