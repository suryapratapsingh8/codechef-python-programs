# cook your dish here
for _ in range(int(input())):
    e=0
    b=0
    r=0
    m=0
    for i in range(4):
        
        dic=(input().split(" "))
        if "Eibar" in dic:
            e=int(dic[1])
        elif("Barcelona" in dic):
            b=int(dic[1])
        elif("Malaga" in dic):
            m=int(dic[1])
        else:
            r=int(dic[1])
    if(b>e and r<m):
        print("Barcelona")
    else:
        print("RealMadrid")