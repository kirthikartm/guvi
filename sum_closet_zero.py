n=int(input())
a=list(map(int,input().split()))
l=max(a)
e,f=0,0
for i in range(0,len(a)):
  for j in range(i+1,len(a)):
    if abs(a[i]+a[j])<l:
      e,f=a[i],a[j]
      l=abs(e+f)
print(e,f)

