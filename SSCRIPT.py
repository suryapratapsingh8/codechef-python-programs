t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=input()
    count=0
    for m in s:
        if m=="*":
            count+=1
        else:
            count=0
        if count==k:
            print("yes")
            break
    else:
        print("no")
    