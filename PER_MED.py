# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=[]
    a,b=1,n 
    for i in range(n//2):
        l.append(b)
        l.append(a)
        a+=1
        b-=1 
    if a==b:
        l.append(a)
    print(*l)
        