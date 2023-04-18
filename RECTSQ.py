# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    for j in range(1,min(a,b)+1): 
        if a%j==0 and b%j==0:
            m=j 
    print((a*b)//(m*m))