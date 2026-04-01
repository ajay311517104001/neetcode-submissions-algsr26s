class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #  Given an array of intergers nums and target integer = 7
        #  nums = [3,4,4,6], target = 7

        #  eg :
            # nums[i] + nums[j] == target where i =! j
            # nums[0] + nums[2] == target 3+4 =7  [0,1] [0,2]
            
            # don'ts 
            # [4,4] , target = 8
            # nums[0] + nums[0] = 8 
        
        #  Naive approach
        #  iterate the nums with starting index 0
        for i in range(0, len(nums)-1):
            #  iterate the nums with the starting index 1
            for j in range(1, len(nums)):
            # if nums[i] + nums[j] == target
                if nums[i] + nums[j] == target and i!=j:
                #  return [i,j]
                    return [i,j]

        