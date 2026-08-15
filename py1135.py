def su(n):   #质数判断函数
    if n<=2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
def allList(n):   #列出某个数所有的可能
    may=[]
    if n==4:
        return [[2,2]]
    for j in range(2,int(n/2)+1):
        if su(j) and su(n-j):
            may.append([j,n-j])
    return may

num=int(input())
nL=[]
for i in range(4,num+1):
    nL.append(allList(i))

for j in nL:
    for p in j:
        str1=str(p[0]+p[1])+"="+str(p[0])+"+"+str(p[1])
        print(str1)
