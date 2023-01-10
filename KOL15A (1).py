# cook your dish here
for i in range(int(input())):
    c=0
    s=input()
    for i in s:
        if i.isdigit():
            c=c+int(i)
    print(c) 
