a,b=map(str,input("").split(" "))
c=0
f=0
for i in range(len(a)):
    if(a[0]==a[1]):
        c+=1
for j in range(len(b)):
    if(b[0]==b[1]):
        f+=1
if(c==f):
    print("yes")
else:
    print("no")
        
