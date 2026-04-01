class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        right = 1
        left = 1
        n = len(nums)
        for i in range(n):
            right*=nums[i]
            left*= nums[n-1-i]
            res = max(res, max(left,right))
            if left == 0:
                left =1
            if right == 0:
                right =1
        return res
