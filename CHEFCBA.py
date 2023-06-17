# cook your dish here
a,b,c,d = map(int,input().split())
print("Possible" if a*d==b*c or a*b==d*c or a*c==d*b else "Impossible")