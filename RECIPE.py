# cook your dish here

def getGCD(a, b):

    while(a > 0 and b > 0):
        if(a > b):
            a = a % b
        else:
            b = b % a
             
    if(a == 0):
        return b
     
    return a
for _ in range(int(input())):
    l=list(map(int,input().split()))
    n=l.remove(l[0])
    gcd =0
    for i in range(len(l)):
        gcd=getGCD(gcd,l[i])
    l[:]=[x//gcd for x in l]
    for i in range(len(l)):
        print(l[i],end=" ")
    print()
