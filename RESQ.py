for _ in range(int(input())):
    n=int(input())
    i=1
    a=set()
    while i*i <=n:
        if n%i==0:
            a.add(abs(n//i-i))
        i+=1
    # print(a)
    print(min(a))