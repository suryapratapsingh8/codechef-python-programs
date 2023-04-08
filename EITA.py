# cook your dish here
for i in range(int(input())):
    d,x,y,z = map(int, input().split(" "))
    
    s1 = 7 * x
    s2 = y*d + (7-d)*z
    
    print(max(s1, s2))