# cook your dish here
for _ in range(int(input())):
    st=input()
    n=len(st)
    c=0
    for i in range(1,n):
        if st[i-1]!=st[i]:
            c=c+1
    print(c//2) if c%2==0 else print((c+1)//2)