# cook your dish here
for _ in range(int(input())):
    s=sorted(input())
    a,c=0,1
    for i in s:
        a+=c*(ord(i)-96)
        c+=1
    print(a)
    
    
    