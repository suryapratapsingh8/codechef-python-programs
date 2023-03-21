# cook your dish here
for _ in range(int(input())):
    A=int(input())
    k=list(str(A))
    if k[0]=='1':
        k.insert(1,'0')
    else:
        k.insert(0,'1')
    print(int(''.join(k)))
        