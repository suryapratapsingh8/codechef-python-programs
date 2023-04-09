# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    o,e=0,0
    for i in l:
        if i&1==0:
            e=e+1 
        else:
            o=o+1 
    print(o*e)