n,t=map(int,input().split())
b=[int(x) for x in input().split()]
b=sorted(b)
x=b[::-1]
print(x[t-1])
