a=int(input(""))
v=a
r=0
while(a!=0):
    re=a%10
    r=re+(r*10)
    a=a//10
if(r==v):
    print("yes")
else:
    print("no")
    
