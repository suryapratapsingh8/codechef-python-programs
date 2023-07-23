# cook your dish here
t=int(input())
for i in range(t):
    n=input()
    for i in range(0,len(n),2):
        if n[i]==n[i+1]:
            print("no")
            break 
    else:
        print("yes")