# cook your dish here
j=int(input())
for h in range(j):
    a=input()
    b=input()
    
    f=0
    
    for i in a:
        if(i in b):
            f=1
            break
    if(f==1):
        print("Yes")
    else:
        print("No")