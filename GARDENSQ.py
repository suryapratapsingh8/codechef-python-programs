
# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split());
    matrix = [];
    for i in range(n):
        matrix.append(input());
    
    count = 0;
    for r in range(n):
        for c in range(m):
            ar = r + 1;
            ac = c + 1;
            
            while (ar < n and ac < m):
                cs = matrix[r][c];
                if (matrix[ar][c] == cs and matrix[ar][ac] == cs and matrix[r][ac] == cs):
                    count += 1;
                ar += 1;
                ac += 1;
    print(count);