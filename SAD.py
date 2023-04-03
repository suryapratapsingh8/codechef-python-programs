r, c = map(int, input().split()) 
matrix_row = []
for _ in range(r):
    matrix_row.append([int(x) for x in input().split()])
matrix_column = []
for i in range(c):
    arr = []
    for j in range(r):
        arr.append(matrix_row[j][i])
    matrix_column.append(max(arr))
possible = set()
for i in range(r):
    current_row = matrix_row[i]
    min_row = min(current_row)
    for j in range(c):
        max_column = matrix_column[j]
        if current_row[j] == min_row and current_row[j] == max_column:
            possible.add(current_row[j])
if possible:
    print(min(possible))
else:
    print('GUESS')
    
            
    
    
    