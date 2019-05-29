a=int(input(""))
s=0
while(a>0):
    x=a%10
    s=s+(x*x)
    a=a//10
print(s)
