a=int(input())
b=[int(a) for a in input().split()]
b.sort()
m=len(b)//2
print(b[m])
