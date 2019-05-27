a=int(input(""))
x=[int(a) for a in input("").split(" ")]
l=len(x)
for i in range(l):
        max=x[0]
        if x[i]>max:
            max=x[i]
print(max)
            
