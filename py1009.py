n=int(input())
s=input()
s=s.split(" ")
for i in range(0,len(s)):
    s[i]=int(s[i])

for i in range(len(s)-1,-1,-1):
    print(s[i],end=" ")