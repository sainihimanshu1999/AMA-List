
def search(matrix,target):
    x = 0
    y = len(matrix[0])-1

    while x<len(matrix) and y>=0:
        if matrix[x][y]>target:
            y-=1
        elif matrix[x][y]<target:
            x+=1
        else:
            return False
    return True
