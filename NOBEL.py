# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    k=list(set(l))
    if len(k)<m:
        print('yes')
    else:
        print('No')
