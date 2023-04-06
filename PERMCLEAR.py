# cook your dish here
for _ in range(int(input())):
    n1=int(input())
    l1=list(map(int,input().split()))
    n2=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    dic={}
    for i in l1:
        if(i in dic):
            dic[i]+=1
        else:
            dic[i]=1
    for i in l2:
        dic[i]-=1
    for i in dic:
        if(dic[i]==1):
            print(i,end=" ")
    print()
    