class Solution:
    # Naive approach
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        # sort the array
        curr_sequence = 1
        nums.sort() # o(nlogN) 
        i=0
        # [1,2,3,5,6]
        # [-2,-1,0,3]
            # 0 1 2 3 4
            #        i
        #  []
        # [2,20,4,10,3,4,5]
        # [2,3,4,4,5,10,20]
        #          i
        #  [1,2]
           
        if nums ==[]:
            return 0
        while i < len(nums):  #o(N)
        # check the current element with next element if the absolute diffrence is 1 
            # if the difference is zero i need to skip those elements
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            if i+1 < len(nums) and abs(nums[i] - nums[i+1]) == 1:
                curr_sequence+=1
            else:
                result = max(result , curr_sequence)
                curr_sequence = 1
            i+=1
        result = max(result , curr_sequence)
        return result

        # Time complexity -  O(nlogn)
        # Space complexity - O(1)
        
        #  increment the current sequence
        # else
        # update the maximum of the over all sequence
        # return the result
        