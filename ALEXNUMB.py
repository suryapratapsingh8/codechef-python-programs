# cook your dish here
for _ in range(int(input())):
    x=int(input())
    l=list(map(int,input().split()))
    k=len(l)-1
    print(k*(k+1)//2)
    
