'''
In rotation question mostly, there exist a reversing or transposing the matrix
'''

def rotate(matrix):

    #reversing
    n = len(matrix)
    left = 0
    right = n-1
    while left<right:
        matrix[left],matrix[right] = matrix[right],matrix[left]
        left +=1
        right -=1

    
    #transposing
    for i in range(n):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    return matrix


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(matrix))