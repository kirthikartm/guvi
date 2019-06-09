a=int(input())
b=[]
for i in range(0,a):
    n=input()
    b.append(n)
s=[]
for i in zip(*b):
    if i.count(i[0])==len(i):
        s.append(i[0])
    else:
        break
print(''.join(s))


    
