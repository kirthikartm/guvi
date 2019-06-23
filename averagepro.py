x=int(input())
l=[int(x) for x in input().split()]
a=int(x/2)
l1=l[:a]
l2=l[a::]
a1=sum(l1)//len(l1)
a2=sum(l2)//len(l2)
if a1==a2:
    print("yes")
else:
    print("no")
