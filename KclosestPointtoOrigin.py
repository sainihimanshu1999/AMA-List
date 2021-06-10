'''
Using heap structure in this question
'''
from heapq import *
import heapq

def closestPoint(points,k):
    heap = []

    for x,y in points:
        dist = -(x*x+y*y)
        if len(heap) == k:
            heappushpop(heap,(dist,x,y))
        else:
            heappush(heap,(dist,x,y))

    return [(x,y) for (dist,x,y) in heap]
        