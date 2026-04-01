class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute force Approach - using sorted - internally uses merge sort - nlogn
        # return nums.sort()


        # optimized approach - since the range is finite 1 - 300 we can use bucket sort 
        #  Bucket sort runs in O(n), for finite range of elements in array

        #  create an array with the max length
        build_arr = [0] * 3
        #  increment in the index
        for i in nums:
            build_arr[i]+=1


        k=0
        #  loop the increment indexed array with length
        for i in range(0,len(build_arr)):
        #  loop the increment index array with element - which is the repetation of elements
            for j in range(0,build_arr[i]):
                nums[k] = i
                k+=1

        #  overwrite the existing array with the index
        
        #  return the overwritten array - saving the space 
        return nums

        