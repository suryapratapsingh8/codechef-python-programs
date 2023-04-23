# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    o=0
    for i in l:
        if i&1!=0:
            o+=1 
    e=n-o 
    ei=n//2 
    oi=n-ei 
    print(min(ei,o)+min(oi,e))