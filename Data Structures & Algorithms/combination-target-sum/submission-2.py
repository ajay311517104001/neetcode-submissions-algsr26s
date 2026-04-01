class Solution:
    # optimal solutionwith sort
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        nums.sort()
        def dfs(index , subset , total):
            if total == target:
                result.append(subset.copy())
                return
            
            for j in range(index , len(nums)):
                if total+nums[j] > target:
                    return
                subset.append(nums[j])
                dfs(j , subset , total+ nums[j])
                subset.pop()






         
         
        dfs(0, [] , 0)
        return result
        