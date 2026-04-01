class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # sample work out 
        #   0 1 2 3 4 5
        # [-1,0,2,4,6,8]
        #         l 
        #       r
                   


        # set the left initial value
        left =0
        # set the right initial value
        right = len(nums)-1
        # check untill the left is lesser than and equal to the right
        while left <= right:
            # find the mid by getting the adding left and right value divide by 2
            mid = (left + right)//2
            #  check if the value is the target return the target
            if nums[mid] == target:
                return mid
            # if target is greater than th mid value
            elif target > nums[mid]:
            # increase the left pointer b 1
                left= mid+1
            # else
            else:
            # decrease the right pointer
                right= mid -1
        # if the target element is still not found out after the loop return -1
        return -1