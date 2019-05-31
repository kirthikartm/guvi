a=input()
a=a.split()
l=[]
for i in a:
    l.append(i)
x=""
for i in range(0,len(l)):
    x=l[i]
    l[i]=x[::-1]
for i in l:
    print(i,end=" ")
