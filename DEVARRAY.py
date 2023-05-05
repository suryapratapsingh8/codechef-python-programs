# cook your dish here
n, q = map(int,input().split())
a = list(map(int,input().split()))
amin = min(a)
amax = max(a)
for t in range(q):
    #print('Yes' if int(input()) in range(amin,amax+1) else 'No')
    print('Yes' if amin <= int(input()) <=amax else 'No')