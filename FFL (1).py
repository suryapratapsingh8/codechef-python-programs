for i in range(int(input())):
    n,s = map(int,input().split())
    list1 = list(map(int,input().split()))
    list2 = list(map(int,input().split()))
    list3 = []
    list4 = []
    j = 0
    while(j<n):
        if(list2[j]==1):
            list3.append(list1[j])
        else:
            list4.append(list1[j])
        j+=1
        
    if(len(list3)==0 or len(list4)==0):
        print("no")
    elif(min(list3)+min(list4)<=(100-s)):
        print("yes")
    else:
        print("no")