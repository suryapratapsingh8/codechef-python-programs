# cook your dish here
for i in range (int(input())):
    r,x=map(int,input().split())
    l=[]
    a=0
    for i in range (r):
        s=str(input())
        c=s.lower()
        if "spoon" in c:
            a=1
        else:
            l.append(c)
    if a==0:
        for i in range (x):
            for j in range (r-4):
                if l[j][i]=="s" and l[j+1][i]=="p" and l[j+2][i]=="o" and l[j+3][i]=="o" and l[j+4][i]=="n":
                    a=1
                    break
                else:
                    continue
    if a==0:
        print("There is indeed no spoon!")
    else:
        print("There is a spoon!")
        
                    
                    