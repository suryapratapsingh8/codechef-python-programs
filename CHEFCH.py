# cook your dish here
a=int(input())
for _ in range(a):
    b=list(input())
    count=0
    for i in range(len(b)-1):
        if b[i]==b[i+1]:
            if b[i+1]=="-":
                b[i+1]="+"
            else:
                b[i+1]="-"
            count+=1
    print(min(count,len(b)-count))