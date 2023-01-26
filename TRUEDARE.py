# cook your dish here
for _ in range (int(input())):
    tr1=int(input())
    tr=list(map(int,input().split()))
    dr1=int(input())
    dr=list(map(int,input().split()))
    ts1=int(input())
    ts=list(map(int,input().split()))
    ds1=int(input())
    ds=list(map(int,input().split()))
    if set(tr)|set(ts) == set(tr) and set(dr)|set(ds) == set(dr):
        print("yes")
    else:
        print("no")