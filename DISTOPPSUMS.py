for i in range(int(input())):
    n=int(input());
    for i in range(n//2,0,-1):
        print(i,end=" ");
    for i in range((n//2)+1,n+1,1):
        print(i,end=" ");
    print()