#TWO TRAINS
for _ in range(int(input())):
    n=int(input())
    t=list(map(int,input().split()))
    print(max(t)+sum(t))