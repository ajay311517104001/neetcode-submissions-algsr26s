class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # declare the need arrays
        #  subset
        subset =[]
        #  result array
        result = []

            # # [1,1,2]
            #    0,1,2

            # [1,1,2]
        
        # Time Complexity - N.2^n
        # space aux - N
        # total space N + 2^n


        nums.sort() #O(nlogN)
        # funtion definition
        def dfs(index , subset):
            # basecase
            if index == len(nums):
                result.append(subset.copy()) # O(N)
                return
            if index >len(nums):
                return 
            # constrain should not have duplicate subset
            
            subset.append(nums[index])
            dfs(index+1 , subset) 
            subset.pop()
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index+=1
            # backtracking
            dfs(index+1, subset)                
        # function call
        dfs(0, subset)
        # dfs(0,[])

        return result