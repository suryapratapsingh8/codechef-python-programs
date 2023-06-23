# cook your dish here
t=int(input())
for i in range(t):
    
    n=int(input())
    l=[]
    s=[]
    for i in range(n):
        s1=input()
        l.append(s1)
        x=s1.split(' ')
        s.append(x[0])
        
    # print(l)
    
    # print(s)
        
    for i in range(len(s)):
        
        if s.count(s[i])>1:
            print(l[i])
            
        else:
            print(s[i])
        