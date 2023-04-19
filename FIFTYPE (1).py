# cook your dish here
for _ in range(int(input())):
    n=int(input())
    c=0
    if n>50:
        k=n-50
        if k%3==0:
            c=k//3
        else:
            c=k//3+2*(k%3) 
    else:
        j=50-n
        if j%2==0:
            c=j//2
        else:
            c=j//2+3
    print(c)