# suspense string
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    l=0
    m=1
    a=[]
    for i in range(n):
        if i%2==0:
            if s[l]=="0":
                a.insert(0,"0")
            else:
                a.append("1")
            l+=1
        else:
            if s[-l]=="1":
                a.insert(0,"1")
            else:
                a.append("0")
            m+=1
    b = "".join(a)
    print(b)