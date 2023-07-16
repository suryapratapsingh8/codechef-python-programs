
t = int(input())

for _ in range(t):
    n = int(input())
    
    s = str(input())
    res = ''
    for i in range(0,n,2):
        
        if s[i:i+2] == '00':
            res += 'A'
        if s[i:i+2] == '01':
            res += 'T'
        if s[i:i+2] == '10':
            res += 'C'
        if s[i:i+2] == '11':
            res += 'G'
    print(res)
        
        