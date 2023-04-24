# cook your dish here
for _ in range(int(input())):
    s=input()
    k=''
    e=0
    a,b=0,0
    for i in s:
        if i=='A':
            a=a+1
            if e!=0 and i=='A' and k=='A':
                a=a+e 
                e=0
                k='A'
            else:
                k='A'
                e=0
        elif i=='B':
            b=b+1
            if e!=0 and i=='B' and k=='B':
                b=b+e 
                e=0
                k='B'
            else:
                k='B'
                e=0
        else:
            e=e+1 
    print(a,b)
                
                
                
            
