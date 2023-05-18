# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n):
        if l[i]==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()