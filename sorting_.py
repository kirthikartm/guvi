a=int(input())
c=[int(a) for a in input().split()]
for i in range(a):
    for j in range(i,a):
        if(c[i]>c[j]):
            t=c[i]
            c[i]=c[j]
            c[j]=t
    print(c[i],end=" ")
