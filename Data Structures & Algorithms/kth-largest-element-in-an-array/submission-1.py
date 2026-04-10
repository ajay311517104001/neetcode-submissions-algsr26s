class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap , n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

        # Time Complexity : O(n) with heapify but for each pop operation it cost O(logn) in worst case if the k = 0, need to pop all so it will me O(nlogn) operation
        # space Complexity : O(1) , heapify does this in place