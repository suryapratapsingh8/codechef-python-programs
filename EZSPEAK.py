# cook your dish here
for t in range(int(input())):
    n=int(input())
    st=input()
    c=0
    flag=False
    vowels=['a','e','i','o','u']
    for i in st:
        if i not in vowels:
            c+=1
        else:
            c=0
        if c>=4:
            flag=True
    if flag:
        print("NO")
    else:
        print("YES")