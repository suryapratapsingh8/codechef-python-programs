# cook your dish here
def avg(a,b):
    c = (a+b)/2
    if(c>=35):
        return 1 
    else:
        return 0

for t in range(int(input())):
    a,b,c = map(int,input().split())
    e1 = avg(a,b)
    e2 = avg(b,c)
    e3 = avg(a,c)
    if(e1 ==1 and e2 ==1 and e3 ==1):
        print("PASS")
    else:
        print("Fail")
