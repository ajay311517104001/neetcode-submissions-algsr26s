"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [ obj.start for obj in intervals]
        ends = [obj.end for obj in intervals]

        starts.sort()
        ends.sort()

        rooms = 0
        s , e = 0 , 0
        room = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                room+=1
                s+=1
            else:
                room-=1
                e+=1
            rooms = max(rooms , room )
        
        return rooms



