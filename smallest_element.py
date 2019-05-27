a=int(input(""))
x=[int(a) for a in input("").split(" ")]
l=len(x)
for i in range(l):
        min=x[0]
        if x[i]<min:
            min=x[i]
print(min)
            
