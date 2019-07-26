a=int(input())
b=[int(a) for a in input().split()]
for i in range(0,len(b)):
  if(b.count(i)==1):
    print(i)
    
