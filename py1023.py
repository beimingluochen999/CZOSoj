num=int(input())

if num==1:
    print("F")
else:
    for i in range(2,int(num**0.5)+1):   #为了保证不超时，遍历跑道开方数即可。不这么做大数会超时
        if num%i==0:   #核心，检查是否有因数
            print("F")
            break
    else:
        print("T")