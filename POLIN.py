# cook your dish here
t=int(input())
for j in range(t):
    h=[]
    v=[]
    ans=0
    n=int(input())
    for i in range(n):
        e=input().split()
        h.append(e[0])
        v.append(e[1])
        #if e[0]==1 and e[1]==0:
            #ans+=1
    h=list(set(h))
    v=list(set(v))
    ans=ans+len(h)+len(v)
    print(ans)