x=int(input())
for i in range(x):
    num=int(input())
    i=list()
    j=1
    for k in range(num):
        i.append(j)
        j+=2
    print(*i)