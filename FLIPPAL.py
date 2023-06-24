# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    a=0
    b=0
    for i in s:
        if i=="0":
            a+=1
        if i=="1":
            b+=1
    if a%2==0 or b%2==0:
        print("yes")
    else:
        print("no")