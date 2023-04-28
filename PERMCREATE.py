# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n<4:
        print(-1)
        
    else:
        l=[1,3,2,4]
        for i in range(5,n+1):
            if i&1==0:
                l.append(i)
            else:
                l.insert(0,i)
        print(l)