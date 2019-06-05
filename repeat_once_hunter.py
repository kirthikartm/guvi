a=int(input())
b=[int(a) for a in input().split()]
c=[]
for i in range(0,a):
    for j in range(i+1,a):
        if(b[i]==b[j]):
            c.append(b[i])
d=list(set(b).difference(set(c)))
for i in d:
       print(i)
            
