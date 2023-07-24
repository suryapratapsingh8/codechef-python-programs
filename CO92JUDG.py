# cook your dish here
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr1=list(map(int,input().split()))
    a=sum(arr)-max(arr)
    bs=sum(arr1)-max(arr1)
    if(a>bs):
        print("Bob")
    elif(a==bs):
        print("Draw")
    else:
        print("Alice")
     