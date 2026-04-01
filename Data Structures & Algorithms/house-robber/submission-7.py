class Solution:
#     # Top down approach - memo
    def rob(self, nums: List[int]) -> int:
        if not nums:
                return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        def dfs(i , cache):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0], nums[1])

            if i in cache:
                return cache[i]
            
            cache[i] = max(dfs(i-1 , cache) , dfs(i-2 , cache)+ nums[i])

            return cache[i]
        
        return dfs(len(nums)-1 , {})


        

        