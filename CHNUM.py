# cook your dish here
T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    b = 0
    c = 0
    for i in A:
        if i>0:
            b+=1 
        elif i<0:
            c+=1 
    if b==N or b==0:
        print(N, N)
    elif b>c:
        print(b, c) 
    else:
        print(c, b)