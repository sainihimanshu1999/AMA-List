'''
we use hash map in this question to find the frequency, and we insert the elements in the odd ven positions
'''
from collections import Counter

def dbarcode(barcodes):
    count = Counter(barcodes)
    i,n=0,len(barcodes)
    result = [0]*n


    for code,freq in count.most_common():
        for _ in range(freq):
            if i>=n:
                i = 1
            result[i] = code
            i +=2

    return result


codes = [1,1,1,2,2,2]
print(dbarcode(codes))
