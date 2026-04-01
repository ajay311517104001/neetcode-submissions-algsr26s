class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Brute force solution 
        #  TC -> O(n) SC -> O(1)
        # mini = nums[0]
        # #  iterate array
        # for i in range(1,len(nums)):
        #     if nums[i] < mini:
        #         mini = nums[i]
        # return mini
        
        #  optimize this solution
            # 0 1 2 3 4 5
        #  [3,4,5,6,1,2]
                    # r
        # l =0        
                    
        # r = len(nums)-1 #5
        # if nums[l] < nums[r]:
        #     return nums[l]
        # else:
        #     while l<=r:
        #         mid = (l+r)//2 # 2 4 3
        #         if nums[mid] > nums[l]:
        #             l=mid+1
        #         elif nums[mid] < nums[r]:
        #             r = mid -1
        #         else:
        #             return nums[mid]
    
    # [4,5,6,7,0,1,2]
            #    l m r
    #    Intution
        res=nums[0] # 1 left has only 2 options , it may be high or it may be low
        l=0
        r = len(nums)-1
        # while l<=r
        while l<=r:
        #  find the mid -> update the res by check which is minimum
            mid = (l + r)//2
            
            res = min(res , nums[mid])
            if nums[l] < nums[r]:
                res = min(res , nums[l])
        # check if the mid is >= left
            if nums[mid]>= nums[l]:
        #  check the right portion
                l = mid+1
        # check if the mid is <= right
            else:
                r= mid-1
        # check the left portion
        return res
