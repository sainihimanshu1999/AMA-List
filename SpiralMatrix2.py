'''
In spiral matrix we habe to print squares of number in spiral(it'll be square matrix)
'''

def spiral2(n):
    matrix = [[None]*n for _ in range(n)]

    left,right = 0,n-1
    top,down = 0,n-1
    num = 1
    while left<=right and top<=down:
        
        for i in range(left,right+1):
            matrix[top][i] = num
            num +=1
        top +=1

        for i in range(top,down+1):
            matrix[i][right] = num
            num +=1
        right -=1
        for i in range(right,left-1,-1):
            matrix[down][i] = num
            num+=1
        down -=1
        for i in range(down,top-1,-1):
            matrix[i][left] = num
            num+=1
        left +=1
    return matrix


print(spiral2(9))