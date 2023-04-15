# cook your dish here
for _ in range(int(input())):
    s=input()
    c=0
    k=''
    for i in s:
        if i not in k:
            c=c+1 
            k=k+i
    print(c)