class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create max heap
        h = []
        for s in stones:
            heapq.heappush(h , -s)
        
        # Iteratively compute the heap
        while len(h) > 1:
            first = heapq.heappop(h)
            second = heapq.heappop(h)
            if abs(first) - abs(second)!=0:
                heapq.heappush(h , -(abs(first) - abs(second)))
        return abs(h[0]) if len(h) == 1 else 0
        