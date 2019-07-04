a=input()
l=[]
for i in range(len(a)):
    b=a.count(a[i])
    l.append(b)
s=l.index(max(l))
print(a[s])
