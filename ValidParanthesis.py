def isValid(self,s):

    maps = {'[':']','(':')','{':'}'}

    stack = []

    for i in s:
        if i in maps:
            stack.append(i)
        elif i in maps.values():
            if not stack or map[stack.pop()] != i:
                return False
    
    return stack == []