'''
Checking if two numbers are anagram or not
'''

def anagram(s,t):
    return sorted(s) == sorted(t)