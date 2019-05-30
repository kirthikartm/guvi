a,b=map(str,input().split())
c=0
for i in range(0,len(a)):
	if a[i]!=b[i]:
		c=c+1
	else:
		continue
if c==1:
	print("yes")
else:
	print("no")
