# cook your dish here
for i in range(int(input())):
        p,q=map(int,input().split())
        if(p+q)%4==0 or (p+q)%4==1:
                print("Alice")
        else:
                print("Bob")