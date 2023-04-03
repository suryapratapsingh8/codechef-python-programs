# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=[]
    for i in range(k,1,-1):
        l.append(n%i)
    print(max(l))