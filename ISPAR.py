# cook your dish here

x = int(input())
ml = []
for r in range(0,x):
    a = str(input())
    a = a.strip()
    m = a.split(" ")
    wer=[]

    for bbv in m:
        wer.append(int(bbv))
    ml.append(wer)
    
for bbc in ml:
    
    if bbc[-1] == 1:
        if bbc[0] %2 == 0:
            print("EVEN")
        else:
            print("ODD")
    else:
        if bbc[-1] == 2:
            print("ODD")
        else:
            print("EVEN")
        
        
    