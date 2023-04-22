# cook your dish here
t = int(input(""))
for _ in range(t):
    n = int(input(""))
    s = input("") # initial state
    r = input("") # final state
    bulb = True
    for i in range(0, n):
        if s[i] != r[i]:
           bulb = not bulb 
    if bulb:
        print(1)
    else:
        print(0)