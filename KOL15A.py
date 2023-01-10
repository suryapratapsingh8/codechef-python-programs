# cook your dish here
for _ in range(int(input())):
    s=input()
    l=[]
    for j in s:
        if (j.isdigit()):
            l.append(j)
    res = [round(float(i)) for i in l]
    print(sum(res))
