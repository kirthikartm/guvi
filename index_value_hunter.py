n=int(input())
c=[int(n) for n in input().split()]
v=[]
for i in range(n):
    if(i==c[i]):
        v.append(c[i])
if(v==[]):
    print("-1")
else:
    print(*v)
        
