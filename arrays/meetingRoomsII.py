class Interval(object):
    def __init__(self, start, end):
        self.start = start 
        self.end = end 
        
class Solution:
    def minMeetingRooms(self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        res, count = 0, 0
        s, e = 0, 0 # the two pointers
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
 


"""
the question asks us to find the maximum number of overlapping meetings at any point in time
"""