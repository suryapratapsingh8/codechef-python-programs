s=input()

n=int(input())
for i in range(n):
    x=input()
    c=0
    for j in x:
        if j not in s:
            c=1 
    if c==1:
        print('No')
    else:
        print('Yes')
    
