class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
         
        i = 0
        n = len(intervals)
        res = []
        # add all interval that come before the new interval 
        while i < n and   intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1
        
        # add all interval that overlaps 
        
        while i < n and  newInterval[1] >= intervals[i][0] :
            newInterval[0] = min(intervals[i][0] , newInterval[0])
            newInterval[1] = max(intervals[i][1] , newInterval[1])
            i+=1
        res.append(newInterval)
        
        #  add at last
        while i < n:
            res.append(intervals[i])
            i+=1
        
        
        return res


