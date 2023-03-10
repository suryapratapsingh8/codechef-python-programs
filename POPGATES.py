t = int(input())


def flip(letter):
    for i in range(len(letter)):
        if(letter[i] == 'T'):
            letter[i] = 'H'
        else:
            letter[i] = 'T'
    
    return letter
for i in range(t):
    n,k = [int(x) for x in input().split()]
    letters = input().split()
    l = letters
    cc = 0
    for j in range(k):
        if l[-1] == 'H':
            l = flip(l[:-1])
        else:
            l = l[:-1]
    for i in l:
        if(i == 'H'):
            cc += 1 
    print(cc)
        
            
            
            