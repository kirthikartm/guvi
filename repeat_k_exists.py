a,b=map(int,input().split())
c=[int(b) for b in input().split()]
for i in range(len(c)):
    if(i==b):
        print("yes")
        break
else:
     print("no")
