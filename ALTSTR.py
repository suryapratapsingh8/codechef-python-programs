# cook your dish here
# cook your dish here

t=int(input())

while t>0:
    n=int(input())
    s=input()
    l=min(s.count("0"),s.count("1"))
    if s.count("0")==s.count("1"):
        print(n)
    else:
        print(2*l+1)
    t=t-1