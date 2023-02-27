# cook your dish here


h = int(input())

t = []

for iin in range(0,h):
    hnc = int(input())
    tfx = str(input())
    
    lrt=[]
    for iix in tfx.split(" "):
        lrt.append(int(iix))
        
    t.append(lrt)
    
for jjd in t:
    jjd.sort()
    ans=0
    if jjd[0] == 0:
        jjd.pop(0)
    if len(jjd) == 1:
        print(-1)
    else:
        jui = jjd[0]
        gcd=1
        for hnu in range(2,jui+1):
            indi=0
            for klr in jjd:
                if klr%hnu != 0:
                    indi = 1
                    break
            if indi == 1:
                continue
            else:
                if hnu>gcd:
                    ans=-1
                    break
                
        print(ans)
                
                
                    
        
        
    
                