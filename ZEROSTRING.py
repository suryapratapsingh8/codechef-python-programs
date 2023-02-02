# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    k=s.count('0')
    d=n-k 
    if k>=d:
        print(d)
    else:
        print(k+1)
