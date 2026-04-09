class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # create a list with the calcualte distance
        # create a max heap out of it
        # filter all the elements in the front down to the k 
        # return the remaning
        h = []
        for x , y in points:
            heapq.heappush(h, [-(x**2+ y**2) , x , y])
            if len(h) > k:
                heapq.heappop(h) 
        res = []
        while h:
            dist, x, y = heapq.heappop(h)
            res.append([x,y])
        return res           
