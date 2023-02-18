# cook your dish here
for _ in range(int(input())):
    j=set(input())
    s=input()
    c=0
    for i in s:
        if i in j:
            c+=1
    print(c)
        