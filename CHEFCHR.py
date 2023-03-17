# cook your dish here
for i in range(int(input())):
    s=input()
    c=0
    for i in range(len(s)-3):
        if set(s[i:i+4])==set('chef'):
            c=c+1
    if c>0:
        print("lovely", c)
    else:
        print("normal")