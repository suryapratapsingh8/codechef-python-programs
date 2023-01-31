# cook your dish here
for _ in range(int(input())):
    n=int(input())
    c=1
    t=1
    for i in range(2,n):
        k=t+i 
        if k<=n:
            c=c+1 
            t=k
            
        else:
            break
    print(c)
        