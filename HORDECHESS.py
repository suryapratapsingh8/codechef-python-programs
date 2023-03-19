# cook your dish 
# cook your dish here
# cook your dish here
MOD = 10 ** 9 + 7
T = int(input())
for cases in range(T): 
    
    N = int(input()) 
    if N % 4 == 0: 
        min_pawns = (N - 1) * (N // 2)
        arrangements = 1
    elif N % 4 == 2: 
        min_pawns = (N - 1) * ((N + 2) // 2)
        arrangements = pow((N + 2) // 4, 2 * (N - 1), MOD)
    elif N % 4 == 3: 
        min_pawns = (N - 1) * ((N + 1) // 2) 
        arrangements = pow((N + 5) // 4, N - 1, MOD)
    elif N % 4 == 1: 
        min_pawns = (N - 1) * ((N + 1) // 2) 
        arrangements = pow((N - 1) // 4, N - 1, MOD)
    print(min_pawns, arrangements)
        
        