n=input()
n=n.split(" ")
for i in range(0,len(n)):
    n[i]=int(n[i])

print(max(n))