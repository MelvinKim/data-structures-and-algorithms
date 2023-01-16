from tracemalloc import start


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
        
class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda i :i.start) # sort the intervals by the start time

        """
        compare adjacent elements, start at 1
        """
        for i in range(1, len(intervals)):      
            interval1 = intervals[i-1]
            interval2 = intervals[i]  
            if interval1.end > interval2.start:
                return False
             
        return True





"""
def can_attend_meetings(intervals):
    # sort the intervals by the start time
    intervals.sort(key=lambda x:x[0]) # 0(n*logn) Time 
    # compare the ending elements of i+1 and i
    for i in range(len(intervals)-1): # O(N) Time
        if intervals[i+1][0] < intervals[i][1]:
            return False
        
    return True
    
    
intervals = [(0,30),(5,10),(15,20)]
print(can_attend_meetings(intervals))
"""