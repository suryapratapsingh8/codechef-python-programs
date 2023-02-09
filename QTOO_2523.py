# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    for i in s:
        c=s.count(i)
        if c>=2:
            print(n-2) 
            break 
        
    else:
        print('-1')