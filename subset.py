a,b=map(int,input().split())
c=[int(a) for a in input().split()]
d=[int(b) for b in input().split()]
p=[]
for i in range(0,len(d)):
    for j in range(0,len(c)):
        if(d[i]==c[j]):
            p.append(d[i])
d=list(d)
if p==d:
    print("YES")
else:
    print("NO")
