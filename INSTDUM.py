t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    k=1
    l=[]
    sumi=0
    count=0
    for i in a:
        sumi+=i
        op=(sumi/k)*100
        if op==100:
            count+=1
        k+=1 
    print(count)
        