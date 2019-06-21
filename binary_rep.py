a=int(input())
b=[int(a) for a in input().split()]
e=[]
for i in b:
    c=bin(i)[2:]
    e.append(c)
e.sort()
e.reverse()
for i in e:
    i=str(i)
    d=int(i,2)
    print(d)
