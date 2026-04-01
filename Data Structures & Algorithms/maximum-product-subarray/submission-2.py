class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        for i in range(0, len(nums)):
            product = nums[i]
            res = max(res, product)
            for j in range(i+1 , len(nums)):
                product*=nums[j]
                res = max(res,product)

            
        return res if res!= float('-inf') else 0