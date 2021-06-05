'''
This question is pretty straight forward but the key is to optimize this question, for that we use
two heaps, max and min heap.
'''
from heapq import *

class MedianFinder:

    def __init__(self):
        self.small = [] #maxheap
        self.large = [] #minheap

    def addNum(self,num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small,-num))
        else:
            heappush(self.small, -heappushpop(self.large,num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0]-self.small[0])/2.0
        else:
            return float(self.large[0])