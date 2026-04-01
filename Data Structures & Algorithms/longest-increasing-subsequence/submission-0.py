class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(i):
            n =len(nums)
            lis = 1

            for j in range(i+1 ,n):
                if nums[i] < nums[j]:
                    lis = max(lis , 1+dfs(j))

            return lis





        return max(dfs(i) for i in range(len(nums)))