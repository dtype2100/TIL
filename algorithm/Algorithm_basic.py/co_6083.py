r,g,b=input().split()   
n=0 
for i in range(int(r)): 
    for j in range(int(g)):
        for k in range(int(b)): 
            print(i,j,k)
            n+=1

print(n)    