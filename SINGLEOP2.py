# cook your dish here
for i in range(int(input())):
    n=int(input())
    s=input()
    i=1
    while(i<n and s[i]=='0' ): #upto the zeroes char in the input
        i+=1
    print(i)