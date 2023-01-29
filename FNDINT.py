# cook your dish here
def distinct(x):
    while x!=0:
        a=str(x%10)
        x=x//10
        y=str(x)
        if a in y:
            return False
    return True
for i in range(int(input())):
    x=int(input())
    y=x+1
    while not distinct(y):
        y+=1
    print(y)