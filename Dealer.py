a=int(input())
x=[int(a) for a in input().split(" ")]
min=x[0]
v=[]
for i in range(1,len(x)):
    if(min>x[i]):
        min=x[i]
        v.append(i)
if(len(v)!=0):
    print("Dealer"+str(v[-1]))
else:
    print("Dealer"+"0")
