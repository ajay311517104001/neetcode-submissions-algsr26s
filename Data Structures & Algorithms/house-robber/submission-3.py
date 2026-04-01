class Solution:
    def rob(self, nums: List[int]) -> int:
        # I can start with index 0 I can run a loop by hopping i+2 indices and maintian one total
        # I can do the same thing witht index one and get the total 
        # return max(both total)
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev2 = nums[0]
        prev1 =max(nums[0] , nums[1])
        for n in range(2 , len(nums)):
            curr = max( prev1 , prev2 + nums[n])
            prev2 = prev1
            prev1 = curr
        return prev1