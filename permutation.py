from itertools import *
S=input() 
p=permutations(S) 
for i in p: 
    print("".join(i))
