# cook your dish here
for no in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    s=set()
    for i in range(n):
        if a[i] in s:
            s.remove(a[i])
            
        else:
            s.add(a[i])
        
        count=max(count,len(s))
    print(count)
     