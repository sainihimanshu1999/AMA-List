'''
A class for the data structrue such that we can do push,pop,top,getmin in constant time
'''

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self,val):
        currMin = self.getMin()
        if currMin == None or val<currMin:
            currMin = val
        self.stack.append((val,currMin))

    def pop(self):
        self.stack.pop()

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self):
        if not self.stack:
            return None
        return self.stack[-1][1]