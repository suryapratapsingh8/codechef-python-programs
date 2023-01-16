a,b=map(int,input().split())
c=[]
for i in range(a):
    c.append(input())
    
for j in range(b):
    d=input()
    for i in c:
        if((i in d) or (len(d)>=47)):
            print('Good')
            break
    else:
        print('Bad')
    
    
