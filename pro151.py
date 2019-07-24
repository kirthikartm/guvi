a=int(input())
b=[int(a) for a in input().split()]
e=[]
d=b.index(max(b))
for i in range(d,len(b)):
    e.append(b[d])
    d=d+1
print(*e)  
print(max(b))
