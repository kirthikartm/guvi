a=int(input())
b=[int(a) for a in input().split()]
c=[]
for i in range(0,a):
    for j in range(i+1,a):
        if(b[i]==b[j]):
            c.append(b[i])
if(len(c)==0):
    print("unique")
else:
    for i in c:
        print(c[0])
        break
            
