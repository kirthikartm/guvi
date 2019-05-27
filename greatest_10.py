a=int(input(""))
x=[int(a) for a in input("").split(" ")]
l=len(x)
max=0
for i in range(l):
        if(x[i]>max):
            max=x[i]
print(max)
        
    
