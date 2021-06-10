def prison(cells,n):  
    seen = set()
    for i in range(n):
        nextcell = nextday(cells)
        nextcell_str = str(nextcell)
        if nextcell_str not in seen:
            seen.add(nextcell_str)
        else:
            return prison(cells,n%i)
        cells = nextcell
        
    return cells

def nextday(cells):
    result = [0]*8
    for i in range(1,7):
        result[i] = int(cells[i-1]==cells[i+1])
    return result


cells = [0,1,0,1,1,0,0,1]
print(prison(cells,7))

    
