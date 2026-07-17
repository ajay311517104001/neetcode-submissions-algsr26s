class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum1 = 0
        # sum2 = 0
        # for n in nums:
        #     sum1+=n
        
        # for i in range(len(nums)+1):
        #     sum2+=i
        
        # return sum2-sum1

        n = len(nums)
        xor = n

        for i in range(n):
            calc = i ^ nums[i]
            xor = calc ^ xor
        return xor

