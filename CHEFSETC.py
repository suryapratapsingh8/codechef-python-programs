
for _ in range(int(input())):
    A = list(map(int, input().split(" ")))[:4]
    if A[0]==0 or A[1]==0 or A[2]==0 or A[3]==0 or A[0]+A[1] == 0 or A[0]+A[2] == 0 or A[0]+A[3] == 0 or A[0]+A[1]+A[2] == 0 or A[0]+A[2]+A[3]==0 or A[0]+A[1]+A[3]==0 or A[1]+A[2]+A[3]==0 or A[1]+A[2] == 0 or A[1]+A[3] == 0 or A[2]+A[3]==0 or A[0]+A[2]+A[3] == 0 or A[0]+A[1]+A[2]+A[3]==0:
            print('Yes')
    else:
        print('No')
            
