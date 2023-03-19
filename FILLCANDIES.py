# cook your dish here
for i in range(int(input())):
    n,k,m=map(int,input().split())
    if(n%(k*m)==0):
        print(n//(k*m))
    else:
        n=n//(k*m)
        print(n+1)# cook your dish 
