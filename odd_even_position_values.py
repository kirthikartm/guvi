a=int(input())
b=[int(a) for a in input().split()]
for i in range(0,a,1):
    if(i%2==0):
        if(b[i]%2!=0):
            print(b[i],end=" ")
    elif(i%2!=0):
        if(b[i]%2==0):
            print(b[i],end=" ")
                
        
