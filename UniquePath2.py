'''
In this question we have to calculate the unique path from top to bottom while we have obstacle in it
'''

def path(matrix):
    m = len(matrix)
    n = len(matrix[0])

    grid = [[0]*n for _ in range(m)]
            
    grid[0][0] = 0 if matrix[0][0] == 1 else 1

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                grid[i][j] = 0
            else:
                if i-1>=0:
                    grid[i][j] += grid[i-1][j]
                if j-1>=0:
                    grid[i][j] += grid[i][j-1]

    return grid[-1][-1]

x = [[0,0,0],[0,1,0],[0,0,0]]
print(path(x))

