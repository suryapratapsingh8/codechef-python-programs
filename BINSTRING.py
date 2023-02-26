T=int(input())
for i in range(T):
    N=int(input())
    S=list(input())
    c=1
    for j in range(len(S)-1):
        if(S[j]!=S[j+1]):
            c+=1
    print(c)    
            
    