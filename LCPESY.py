# cook your dish here
t = int(input())
for i in range(t):
    x = str(input())
    y = str(input())
    count = 0
    for i in x:
        if i in y:
            y = y.replace(i,"",1)
            count +=1
    print(count)    