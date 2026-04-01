class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # choice : nums can use the same value again and again to get the result
        # basecase : equal to target sum add the subset
        # backtrack : include or exclude
        # constrain : equal to target sum 
        
        subset = []
        result = []

        def dfs(index, subset , total):
            # basecase and constrain
            if total == target:
                result.append(subset.copy())
                return
            if index > len(nums)-1 or total > target:
                return
            
            # backtrack
            subset.append(nums[index])
            dfs(index , subset, total+nums[index])
            subset.pop()
            dfs(index+1 , subset , total)
                

        dfs(0 , subset , 0)
        return result