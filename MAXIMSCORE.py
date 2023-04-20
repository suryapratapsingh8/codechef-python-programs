for g in range(int(input())):
    r=int(input())
    A=list(map(int,input().split()))
    lt=[]
    for i in range(0,r-1):
        lt.append(max(abs(A[i]-A[i-1]),abs(A[i]-A[i+1])))
        lt.append((abs(A[0]-A[1])))
        lt.append((abs(A[-1]-A[-2])))
    print(min(lt))
