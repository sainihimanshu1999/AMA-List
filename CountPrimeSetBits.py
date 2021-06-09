'''
In number 10^6 there are at most 20 bits
'''

def countSetPrime(left,right):
    primes = {2,3,5,7,11,13,17,19}

    def setbits(n):
        count = 0
        while n:
            n = n&(n-1)
            count +=1
        return count

    return sum(setbits(x) in primes for x in range(left,right+1))