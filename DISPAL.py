# cook your dish here
for i in range(int(input())):
    n,x=map(int,input().split())
    
    if x==1:
        print('a'*n)
    elif n%2:
        if x>(n+1)//2:
            print(-1)
        else:
            s=''
            for i in range(97,97+x):
                s+=chr(i)
            s+='a'*((n+1)//2-len(s))
            s1=s[:len(s)-1]
            s+=s1[::-1]
            print(s)
    else:
        if x>n//2:
            print(-1)
        else:
            s=''
            for i in range(97,97+x):
                s+=chr(i)
            if len(s)!=n//2:
                s+="a"*((n)//2-len(s))
            s+=s[::-1]
            print(s)