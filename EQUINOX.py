# cook your dish here
for _ in range(int(input())):
    n,t,a=map(int,input().split())
    sarthak=0
    anu=0
    l=['E','Q','U','I','N','O','X']
    for i in range(n):
        s=input()
        if s[0] in l:
            sarthak+=t  
            
        else:
            anu+=a 
    if sarthak>anu:
        print('SARTHAK')
    elif anu>sarthak:
        print('ANURADHA')
    else:
        print('DRAW')