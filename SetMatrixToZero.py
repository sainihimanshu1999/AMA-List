'''
if we find any zero in matrix we have to make that whole row and col zero
'''

def zero(matrix):
    m = len(matrix)
    n = len(matrix[0])

    rowz = [False]*m
    colz = [False]*n

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rowz[i] = True
                colz[i] = True

    for i in range(m):
        for j in range(n):
            if rowz[i] or colz[j]:
                matrix[i][j] = 0

    return matrix


matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(zero(matrix))
