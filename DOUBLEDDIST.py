# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 'NO'
    for i in range(1,len(a)-1):
        ar = a[i]-a[i-1]
        b = a[i+1] - a[i]
        if ar == 2*b or b == 2*ar:
            ans = "Yes"
        else:
            ans = "No"
            break
    print(ans)
        
