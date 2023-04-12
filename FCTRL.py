for t in range(int(input())): 
    count = 0
    n = int(input())
    while(n!=0):
        count += n//5
        n//= 5
    print(int(count))