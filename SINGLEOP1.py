# Single operation
for i in range(int(input())):
    n=int(input())
    s=input()
    i=1
    while(i<n and s[i]=='1' ):
        i+=1
    print(i)
