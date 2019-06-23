a=int(input())
b=[int(a) for a in input().split()]
c=sorted(b)
d=c[::-1]
p=d[0:2]
print(sum(p))
    
