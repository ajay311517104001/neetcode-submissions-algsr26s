class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for this given example it says abs(i-j)<=k where k i my window size

        # k is not the actual window size since the window deals with the index so 
        '''0-3 <=3 
           1-4 <=3
           basically it is k+1 window size
        '''

        # my outer loop runs len(nums) - k+1 = 4-4=0

        for L in range(0,len(nums)):
            for R in range(L+1 ,min(len(nums), L+k+1)):
                if nums[L] == nums[R]:
                    return True
        return False
        