class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # its a dp problem 
        #  How the greedy solutions work??
        goal = len(nums)-1
        for i in range(len(nums)-2 , -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False