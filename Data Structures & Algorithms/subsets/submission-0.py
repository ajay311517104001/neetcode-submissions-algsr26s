class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currSet , resultSet = [], []
        # call the helper function
        self.helper(0, nums , currSet , resultSet)
        # return the resultSet
        return resultSet

    # [1,2,3]
    0 # [1]        []
    1 # [1,2]         [1]
    2 # [1,2,3] [1,2]  [1,3] [1]    [] 
    3 # 
    def helper(self, index , nums , currSet , resultSet):
        if index == len(nums):
            resultSet.append(currSet.copy())
            return 

        currSet.append(nums[index])
        # call helper by incrementing it , nums , currset and resultSet
        self.helper(index+1 , nums , currSet , resultSet)
        currSet.pop()
        self.helper(index+1 , nums , currSet , resultSet)

        

        