numRows = 6

if numRows == 1:
    print([[1]])


pascal_tri = [[1] * (n+1) for n in range(numRows)]

index_row = 0

i = 0
j = 1

while index_row < numRows - 1:
    current_row = pascal_tri[index_row]
    if len(current_row) > 1:
        if j < len(pascal_tri[index_row + 1]) - 1:
            pascal_tri[index_row+1][j] = pascal_tri[index_row][i] + pascal_tri[index_row][j]
            i += 1
            j += 1
        else:
            index_row += 1
            i = 0
            j = 1   
    else:
        index_row += 1
        i = 0
        j = 1  

inde         

print(pascal_tri)



