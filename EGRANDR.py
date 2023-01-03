# Andrash and Stipendium

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    t = sum(l)
    if l[n-1]==5 and l[0]!=2 and t/n>=4:
        print('Yes')
    else:
        print('No')
    