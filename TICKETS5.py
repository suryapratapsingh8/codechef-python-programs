# cook your dish here
for _ in range(int(input())):
    s=list(input())
    if(len(set(s))==2):
        print("YES")
    else:
        print("NO")