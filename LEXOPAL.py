# cook your dish here
import math
for i in range(int(input())):
    s=input()
    st=''
    c=0
    r=len(s)
    r1=int(r/2)
    r2=math.ceil(r/2)
    l=list(s)
    l1=list(s[:r1])
    s3=s[r2:]
    l2=list(s3[::-1])
    for i in range(len(l1)):
        if l1[i]=='.' and l2[i]!='.':
            l1[i]=l2[i]
        elif l1[i]!='.' and l2[i]=='.':
            l2[i]=l1[i]
        elif l1[i]=='.' and l2[i]=='.':
            l1[i]=l2[i]='a'
        else:
            if l1[i]!=l2[i]:
                c=1
                break
    if(c!=1):
        if(r%2!=0):
            if(l[r1]=='.'):
                l1.append('a')
            else:
                l1.append(l[r1])
        l1=l1+l2[::-1]
        for x in l1:
            st+=x
        print(st)
    else:
        print("-1")