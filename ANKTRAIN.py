# cook your dish here
tp = [('3UB','6UB'),('2MB','5MB'),('1LB','4LB'),('7SL','8SU')]
tpr = [(y,x) for x,y in tp]
tp = tp + tpr
tpd = dict()
tpd = {int(x[0][0]):(int(x[1][0]),x[1][1:]) for x in tp}

for n in range(int(input())):
    s = int(input())
    wagon = (s-1)//8
    seat = s%8 if s%8 else 8
    s,co = tpd[seat]

    print(wagon*8+s,co,sep='')