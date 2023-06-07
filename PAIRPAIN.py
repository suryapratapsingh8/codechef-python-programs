# cook your dish here
for _ in range(int(input())):
    len = int(input())
    arr= list(map(int,input().split()))
    a=arr.count(1)
    b=arr.count(2)
    print(a*(len-a)+a*(a-1)//2+b*(b-1)//2)