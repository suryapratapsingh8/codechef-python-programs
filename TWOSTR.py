# Chef and wildcardmatching 
for _ in range(int(input())):
    s1=input()
    s2=input()
    for i in range(len(s1)):
        if s1[i]=='?' or s2[i]=='?':
            continue 
        elif s1[i]!=s2[i]:
            print('No')
            break 
    else:
        print('Yes')
