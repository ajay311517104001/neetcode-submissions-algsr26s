class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # # Brute force approach - TC - O(nlogn) , space - O(K)
        # unique = sorted(set(nums)) # to handle negative elements we are sorting and to remove duplicates we are using set
        # #  set doesn't garentee its order. it remove duplicates and when it return i doesn't maintain any order
        # nums[:len(unique)] = unique
        # return len(unique)


        #  optimal solution - using Two pointers
        # [1,2,3,3,4]
        #        L
        #          R
        #  if the incoming array size is 2 means below logic will apply
        #  In therory we know the first element is already sorted so we start with the second one
        # [2,10,30,30,30,30]
        #           L  
        #             R
        l,r = 1,1
        while r <len(nums):
            #  check for its previos value if it is not same
            if nums[r] == nums[r-1]:
                r+=1
            else:
                nums[l] = nums[r]
                l+=1
                r+=1
        return l

   
        