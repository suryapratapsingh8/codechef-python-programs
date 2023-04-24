# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=[]
    
    for x in range(m):
        arr.append(list(map(int,input().split())))

    s=[]
    a=[]
    for i in range(m-1,-1,-1):
        if arr[i][0] not in s and arr[i][1] not in s:
            s.append(arr[i][0])
            s.append(arr[i][1])
            a.append(i)
        
    a.sort()  
    print(*a)