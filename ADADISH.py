# cook your dish here
t = int(input())

for _ in range (t):
    n = int(input())
    c = list(map(int,input().split()))
    a=b=0
    c.sort(reverse=True)
    for i in range (n):
        if(a<b):
            a+=c[i]
        else:
            b+=c[i]
    
    print(max(a,b))
