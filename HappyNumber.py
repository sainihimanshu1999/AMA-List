
def happy(n):
    seen = (n)
    while n!= 1:
        n = sum(int(n)**2 for i in str(n))
        if n in seen:
            return False
        else:
            seen.add(n)
    return True