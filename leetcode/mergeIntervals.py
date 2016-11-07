# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # edge cases
        if len(intervals) == 0:
            return []
        elif len(intervals) == 1:
            return [intervals[0]]
        
        # sort the intervals by starting time
        intervals.sort(key=lambda x: x.start)
        
        mergedIntervals = []
        
        # start with first as current
        currentInterval = intervals[0]
        
        # loop over all intervals
        for nextInterval in intervals[1:]:
            # if beginning of next overlaps, then we'll take the max of the ends and merge
            if currentInterval.end >= nextInterval.start:
                currentInterval.end = max(nextInterval.end, currentInterval.end)
                
            # otherwise intervals don't overlap
            else:
                mergedIntervals.append(currentInterval)
                currentInterval = []
                currentInterval = nextInterval
                
        # make sure we get the last one
        mergedIntervals.append(currentInterval)
        
        return mergedIntervals
            
            
        