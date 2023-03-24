# cook your dish here
for _ in range(int(input())):
    l=list(map(str,input().split()))
    s=''
    for i in range(len(l)-1):
       k= l[i][0].capitalize()
       s=s+k+'. '
    s=s+l[-1].capitalize()   
    print(s)