from collections import Counter

# dl is the difficulty level of each question
def dl(string,p):
    q = int(string)
    if q >= p//2:
        return 'cakewalk'
    elif q <= p//10:
        return 'hard'
    else:
        return 'neither'    
    
for _ in range(int(input())):
    n, p = map(int,input().split())
    a = Counter(map(dl,input().split(),[p]*n))
    print('yes' if a['hard']==2 and a['cakewalk']==1 else 'no')