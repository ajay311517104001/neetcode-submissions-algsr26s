class Solution:
     def subsets(self, nums: List[int]) -> List[List[int]]:
        #  we'll try to implement with the dfs approach
        currSet , resultSet =[], []
        def dfs(index):
            # if the index > = len(nums)
            if index >= len(nums):
            #  add the currset to the result set
                resultSet.append(currSet.copy())
            # return
                return 

            # add the value to the currset
            currSet.append(nums[index])
            # call dfs(i+1 , nums)
            dfs(index+1)
            currSet.pop()
            dfs(index+1)
            # pop element from the currset
            # call dfs(i+1 , nums)



        dfs(0)
        return resultSet

    # # TC-> O(n.2^n)for each and every element in the array there are two possibilitis for N elements it is O(N.2^n)
    # # Space -> O(n . 2^n) where n is the number of possible subsets
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     currSet , resultSet = [], []
    #     # call the helper function
    #     self.helper(0, nums , currSet , resultSet)
    #     # return the resultSet
    #     return resultSet

    # # # [1,2,3] - > 2^N
    # # 0 # [1]        []
    # # 1 # [1,2]         [1]
    # # 2 # [1,2,3] [1,2]  [1,3] [1]    [] 
    # # 3 # 
    # def helper(self, index , nums , currSet , resultSet):
    #     if index >= len(nums):
    #         resultSet.append(currSet.copy()) # this has N N spaces created for copying
    #         return 

    #     #  for each call it created 2 variants means it is exponential 2^n
    #     # 2^n spaces are created while making subset
    #     currSet.append(nums[index])
    #     # call helper by incrementing it , nums , currset and resultSet
    #     self.helper(index+1 , nums , currSet , resultSet)
    #     currSet.pop()
    #     self.helper(index+1 , nums , currSet , resultSet)

        

        