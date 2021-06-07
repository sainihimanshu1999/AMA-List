'''
Read More about gray code, in short it is just a mirror image of reversed decond half of elements
'''

def graycode(n):
    result = [0]
    for i in range(n):
        result += [x+pow(2,i) for x in reversed(result)]
    return result