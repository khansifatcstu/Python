matrix=[[1,1,1],[1,1,1],[1,1,1]]
row=int(input('Enter the row number:'))
column=int(input('Enter the column number:'))
matrix[row-1][column-1]='X'
for row in matrix:
    print(" ".join(map(str, row)))
