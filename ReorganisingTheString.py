'''
We have to reorganise the string so that no same character be same together, ans we use heaps in this question 
heaps usage is very clever
'''
from heapq import heappop, heappush, heappushpop
import heapq
def reorganise(s):
    if not s:
        return ''

    dic = {}

    for char in s:
        dic[char] = dic.get(char,0)+1

    heap = []

    result = ''

    for i in dic:
        heappush(heap,(-dic[i],i))

    while len(heap)>1:
        f1,c1 = heappop(heap)
        f2,c2 = heappop(heap)

        result += c1
        result += c2

        if abs(f1)>1:
            heappush(heap,(f1+1,c1))
        if abs(f2)>1:
            heappush(heap,(f2+1,c2))

    if heap:
        f,c = heap[0]
        if abs(f)>1:
            return ''
        else:
            result+=c

    return result

s = "aaab"
print(reorganise(s))
#"aaab"
