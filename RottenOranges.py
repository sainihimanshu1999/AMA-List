'''
In this question we use graph logic and basically use bfs, we have to find distance from each rotten oragnge
to the fresh orange and using levels to calculate this time or distance
'''

from collections import deque

def rottenOranges(grid):
    m,n = len(grid),len(grid[0])
    fresh = 0
    queue = deque()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i,j))

            if grid[i][j] == 1:
                fresh +=1
    
    print


    level = 0
    moves = [[1,0],[-1,0],[0,1],[0,-1]]

    while queue:
        level += 1
        for _ in range(len(queue)):
            x,y = queue.popleft()
            for dx,dy in moves:
                if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy]==1:
                    fresh -=1
                    grid[x+dx][y+dy] = 2
                    queue.append((x+dx,y+dy))

    return -1 if fresh != 0 else max(level-1,0)


grid = [[2,1,1],[1,1,0],[0,1,1]]
print(rottenOranges(grid))
