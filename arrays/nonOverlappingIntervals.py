def eraseOverlapIntervals(intervals):
    count, slow, fast = 0, 0, 1
    while fast < len(intervals):
        if intervals[slow][1] > intervals[fast][0]:
            count += 1
        else:
            slow = fast

        fast += 1            
    return count

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))