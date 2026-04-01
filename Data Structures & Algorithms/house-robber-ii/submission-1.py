class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def helper(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            prev2 = nums[0]
            prev1 = max(nums[0] , nums[1])
            i = 2
            while i < len(nums):
                curr = max(prev1 , prev2 + nums[i])
                prev2 = prev1
                prev1 = curr
                i+=1
            return prev1

        return max( helper(nums[:len(nums)-1]), helper(nums[1:]))