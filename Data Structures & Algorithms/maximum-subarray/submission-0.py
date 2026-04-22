class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # I only add it only my currsum is positive
        #  i will reset my curr sum when I see the current sum < 0

        curr_sum = 0
        max_sum = nums[0]
        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum+=n
            max_sum = max(curr_sum , max_sum)
        return max_sum

        