a=input("")
l=len(a)
s=""
for i in range(l):
    for j in range(l):
        if(a[i]<=a[j]):
            s=s+a[i]
            print(s)
        
