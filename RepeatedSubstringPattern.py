'''
In any string, if we twice the string (s+s) and remove first and last element from it then if s is present in that, 
then we can say that repeated pattern is present in the string
'''

def substring(s):
    return s in (s+s)[1:-1]



s = 'abab'
print(substring(s))