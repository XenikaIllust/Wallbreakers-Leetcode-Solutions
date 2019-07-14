"""
Solution implemented by sorting based on interval start value.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda item: item[0])
        
        i = 1
        
        while i < len(intervals):
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i] = [min(intervals[i-1][0], intervals[i][0]), max(intervals[i-1][1], intervals[i][1])]
                del intervals[i-1]
                i -= 1
            
            i += 1
            
        return intervals
