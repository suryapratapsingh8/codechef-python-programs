a=int(input())
while(a):
    len=int(input())
    nums=[int(i) for i in input().split(' ')]
    if(sum(nums)%2==1):
        print("NO")
    else:
        print("YES")
    a-=1