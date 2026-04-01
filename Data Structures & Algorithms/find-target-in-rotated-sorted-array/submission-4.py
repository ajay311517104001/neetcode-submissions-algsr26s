class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # optimal approach
        # we need to check for the target
        # l=0
        # r = len(nums)-1
        # res = 0
        # while l<=r:
        #     if nums[l] < nums[r]:
        #         mid = (l+r)//2
        #         if target == nums[mid]:
        #             res =mid
        #         # if target <= nums[mid] and target >= nums[l]:
        #         if  nums[mid] >= nums[l] and ( nums[l] >= target and target<nums[mid]):
        #             r=mid-1
        #         else:
        #             l=mid+1
        # return -1
        # #  find the mid check if that is target
        # # take thr right portion
        # # check if the mid is the target
        # else take the mid left portion is the target



        # find the mid section of the array
        l=0
        r=len(nums) -1
        while l<=r:
        # check if the mid is our target
            mid = (l+r)//2
        #  check if it is in increasing order means mid is greater than left
            if nums[mid] == target:
                return mid
        # check if the target is greater than mid or if the target is less than the left
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if target < nums[mid] or target > nums[r]:
                    r=mid-1
                else:
                    l=mid+1
        #  move the left to right and make the right portion
        # else
        return -1
        # if the target is < than the mid and greater than the left 
        # make the left portion
