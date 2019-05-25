a=[int(a) for a in input("").split()]
b=[int(b) for b in input("").split()]
l1=len(a)
l2=len(b)
sum=0
for i in range(0,l1):
    sum=sum+b[i]
print(sum)
    
