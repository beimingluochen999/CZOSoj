num=float(input())
m=0

if num<=15:
    m=round(num/1.5,2)  #小于10的部分计算
else:
    m+=round(15/1.5,2)+round((num-15)/2.5,2)

print(format(m,'.2f'),end="")   #输出，  .2f  保障输出精度