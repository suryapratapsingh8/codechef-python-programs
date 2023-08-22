# cook your dish here
T = int(input())

for tc in range (T):
    N = int(input())
    A = list(map(int , input().split()))
    sa = [1]*N
    for i in range (N-2,-1,-1):
        if (A[i]*A[i+1] < 0):
            sa[i] = sa[i+1]+1
        else:
            sa[i] = 1
    print(*sa)
        
        
