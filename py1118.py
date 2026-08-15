def isCorrect(num):
    if num**2<1000000 or num**2>9999999:
        return False
    a=list(str(num**2))
    if len(a)!=len(set(a)):
        return False
    return True

s=input()
s=s.split(" ")
mi=int(s[0])
ma=int(s[1])
del s

for i in range(mi,ma+1):
    if isCorrect(i):
        print(i)

