# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    
    count_one=a.count(1)
    count_minus_one=a.count(-1)
    
    if abs(count_one-count_minus_one)<2:
        print("YES")
    elif abs(count_one-count_minus_one)==2:
        if count_one%2==0 and count_minus_one%2==0:
            print("YES")
        else:
            print("NO")
            
    else:
        print("NO")
    
