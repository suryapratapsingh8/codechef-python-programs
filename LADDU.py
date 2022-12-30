# LADDU
for _ in range (int(input())):
    a,n=input().split()
    s=int(a)
    lad=0
    for i in range(s):
        con = input().split()
        if len(con) == 2:
            num = int(con[1])
        con = con[0]
        if con == 'CONTEST_WON':
            lad += 300
            if num < 20:
                lad += (20 - num)
        elif con == 'TOP_CONTRIBUTOR':
            lad += 300
        elif con == 'BUG_FOUND':
            lad += num
        elif con == 'CONTEST_HOSTED':
            lad += 50
    if n == 'INDIAN':
        print(lad//200)
    else:
        print(lad//400)