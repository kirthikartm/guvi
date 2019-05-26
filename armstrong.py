a,b=map(int,input("").split())
for i in range(a,b):
    s=0
    l=len(i)
    t=i
    while(t>0):
        x=t%10
        s=s+(x**l)
        t=t//10
    if(s==i):
        print(i,end=" ")
