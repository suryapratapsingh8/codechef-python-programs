#CHECK ALGORITHM

for _ in range(int(input())):
    S=list(input())
    S.append('0')
    c=0
  
    cc=1
    x=S[0]
    for i in S[1::]:
        if i==x:
            cc+=1
        else:
            c+=len(str(cc))+1
            cc=1
            x=i
  
    if c<len(S)-1:
        print("YES")
    else:
        print("NO")
