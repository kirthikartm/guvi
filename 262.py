a=int(input())
b=[int(a) for a in input().split()]
b.sort()
b.reverse()
c=[]
d=[]
e=[]
for i in range(0,len(b),1):
  c.append(b[i])
for j in range(len(b)-1,-1,-1):
  d.append(b[j])
n=len(b)//2
for i in range(n):
  e.append(c[i])
  e.append(d[i])
print(*e)
  
