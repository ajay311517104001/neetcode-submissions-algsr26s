class Solution:
    # 4 [1,2,3,4,5] if target less than l and greater than the mid -> explore the right portion

    # 4 [2,3,4,5,1] if mid == target return 
 
    #4 [3,4,5,1,2] if left portion sorted and if target is greter than equal to left and lesser than equal to mid - left portion else right portion

    # 4 [4,5,1,2,3] if right portion is sorted target is greater than equal to mid and lesser than equal to right right portion if not left portion

    #4 [5,1,2,3,4] 
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif (nums[l] <= nums[mid]):
                if (target >= nums[l] and target <= nums[mid] ):  
                    # explore the left portion
                    r = mid-1
                else:
                    l=mid+1
            else:
                # expore the right portion
                    if(target >= nums[mid] and target <= nums[r] ):
                        l=mid+1
                    else:
                        r = mid-1
        return -1