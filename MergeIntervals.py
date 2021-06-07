
def merge(intervals):
    intervals = sorted(intervals)
    i = 0
    while i<(len(intervals)-1):
        if intervals[i][-1]>intervals[i+1][0]:
            intervals[i][-1] = max(intervals[i][-1],intervals[i+1][-1])
            del intervals[i+1]

    return intervals