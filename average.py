a=int(input(""))
b=[int(a) for a in input("").split()]
l=len(b)
s=0
for i in range(l):
    s=s+b[i]
    r=s//l
print(r)
