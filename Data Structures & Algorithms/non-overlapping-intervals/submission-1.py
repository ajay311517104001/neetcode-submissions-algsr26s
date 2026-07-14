class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # need to remove minimum so that the intervals remain non-overlapping. 
        
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0
        for start , end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res +=1
                prevEnd = min(end , prevEnd)
        return res