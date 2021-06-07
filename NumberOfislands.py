
def islands(grid):
    m = len(grid)
    n = len(grid[0])

    count =0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(i,j,grid)
                count+=1
    return count


def dfs(i,j,grid):
    m = len(grid)
    n = len(grid[0])

    if 0<=i<m and 0<=j<n and grid[i][j]=='1':
        grid[i][j] = 0
        dfs(i+1,j,grid)
        dfs(i-1,j,grid)
        dfs(i,j+1,grid)
        dfs(i,j-1,grid)


matrix = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(islands(matrix))
