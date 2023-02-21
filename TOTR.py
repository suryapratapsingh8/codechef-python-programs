# cook your dish here
T,M=(input().split())
for j in range(int(T)):
    S=list(input())
    P3=[]
    for i in range(len(S)):
        P=ord(S[i])
        if(P>=65 and P<=90):
            P1=P-64
            P2=M[P1-1].upper()
            P3.append(P2)
    #print(P2)
        elif(P>=97 and P<=122):
            P1=P-96
            P2=M[P1-1]
            P3.append(P2)
        elif(S[i]==' '):
            P3.append('_')
        elif(S[i]=='_'):
            P3.append(' ')
        else:
            P3.append(S[i])
        
    print(''.join(P3))
        
    