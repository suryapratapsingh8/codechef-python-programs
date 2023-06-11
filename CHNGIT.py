for i in range(int(input())):
    n=int(input())
    A=[int(n) for n in input().split()]
    maxim=max(A,key=A.count)
    print(n-A.count(maxim))