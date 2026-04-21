class MedianFinder:

    def __init__(self):
        # max heap - left 
        # min heap - right

        self.maxHeap = []
        self.minHeap = []

        

    def addNum(self, num: int) -> None:
        # by default add it to the max heap
        heapq.heappush(self.maxHeap , -1 * num)

        # check the head of max heap should be < head of minHeap
        if ( self.maxHeap and self.minHeap 
            and (-1 * self.maxHeap[0]) > self.minHeap[0]):
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap , (-1 * val)) 

        # check its size and re organize
        if len(self.maxHeap) > len(self.minHeap)+1:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap , (-1 * val))

        if len(self.minHeap) > len(self.maxHeap)+1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap ,  (-1 * val))
        

    def findMedian(self) -> float:
        # if it is going to be odd check which has odd and return them 

            

        # if it is even get the head of two heaps and return 
        if len(self.maxHeap) > len(self.minHeap):
            return float(-1 * self.maxHeap[0])
        if len(self.minHeap) > len(self.maxHeap):
            return float(self.minHeap[0])
        return  ((-1 * self.maxHeap[0]) +  self.minHeap[0])/2

        
        