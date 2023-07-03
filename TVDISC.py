# cook your dish here
T = int(input())
for i in range(T):
    a,b,c,d = map(int, input().split())
    f = a-c
    s = b-d
    if (f<s):
        print("first")
    elif (f==s):
        print("any")
    else:
        print("second")