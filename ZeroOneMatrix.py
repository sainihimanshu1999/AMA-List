'''
0 1 matrix question is similar to as far from land as possible, it can be done by two methods one is BFS and other 
is just basic operations
'''

#Basic Matrix operation

from typing import Collection


def zeroone(matrix):
    m,n = len(matrix),len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j]!=0:
                matrix[i][j] = float('inf')
                if i> 0 and matrix[i-1][j]+1<matrix[i][j]:
                    matrix[i][j] = matrix[i-1][j]+1
                if j>0 and matrix[i][j-1]+1<matrix[i][j]:
                    matrix[i][j] = matrix[i][j-1]+1


    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if matrix[i][j]!=0:
                if i+1<m and matrix[i+1][j]+1<matrix[i][j]:
                    matrix[i][j] = matrix[i+1][j]
                if j+1<n and matrix[i][j+1]+1<matrix[i][j]:
                    matrix[i][j] = matrix[i][j+1]+1
        
    return 
    


#BFS method
from collections import deque
def zeroone1(matrix):
    m,n = len(matrix),len(matrix[0])
    q = deque()
    visited = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                q.append((i,j))
                visited.add((i,j))


    while q:
        x,y = q.popleft()
        for dirr in [(1,0), (-1,0), (0,1), (0,-1)]:
            newX,newY = x+dirr[0],y+dirr[1]
            if 0<=newX<m and 0<=newY<n and (newX, newY) not in visited:
                matrix[newX][newY] = matrix[x][y] + 1
                visited.add((newX, newY))
                q.append((newX, newY))

    return matrix



mat = [[0,0,0],[0,1,0],[1,1,1]]
print(zeroone1(mat))



