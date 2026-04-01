class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #  i am taking a input array of nums =[1,2,4,6]
        #  return the ouput where each element in the output array
        #  is the product all the element in array except itself

        result_arr =[]
        current_product = 1
        #  iterate the nums
        for i in range(0,len(nums)):
            #  iterate the nums:
            for j in range(0, len(nums)):
                if i!=j:
                   current_product = current_product * nums[j]
            #  put that to the result array

            result_arr.append(current_product)
            current_product = 1
        #  return the array
        return result_arr


          
        