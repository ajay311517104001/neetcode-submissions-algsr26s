class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #  i am taking a input array of nums =[1,2,4,6]
        #  return the ouput where each element in the output array
        #  is the product all the element in array except itself

        # Brute force approach -> T.C -> O(n^2) , SC -> O(N)
        # result_arr =[]
        # current_product = 1
        # #  iterate the nums
        # for i in range(0,len(nums)):
        #     #  iterate the nums:
        #     for j in range(0, len(nums)):
        #         if i!=j:
        #            current_product = current_product * nums[j]
        #     #  put that to the result array

        #     result_arr.append(current_product)
        #     current_product = 1
        # #  return the array
        # return result_arr

        #Optimized soultion with divison operation , Lesson : if the input array has zero it will make the result array zero, not stable approach
        #  get the over all multiplication of the array
        # product = 1
        # for num in nums:
        #     if num!=0:
        #         product*=num

        # # iterate thru the array and divide it with the overall multiplication and insert it in the same
        # #  input array
        # count_zero = 0
        # for i in range(0,len(nums)):
        #     if nums[i] ==0:
        #         count_zero+=1

        # if count_zero == 0:
        #     for i in range(0,len(nums)):
        #         nums[i] = int(product / nums[i])
        #     return nums
        # elif count_zero == 1:
        #     for i in range(0,len(nums)):
        #         if nums[i]==0:
        #             nums[i] = int(product)
        #         else:
        #             nums[i] =0
        #     return nums
        # elif count_zero > 1:
        #     return [0]*len(nums)
            
        #  return nums
        

        # using prefix and postfix sums
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        result = [1]*len(nums)
        # # calculate the prefix and postfix sum and put them in the array
        # nums =  [1,2,4,6]
        # prefix= [1,1,1,1]
        # working= [1,1,2,8]
        #        = [48,24,6,1]
        # index =  0,1,2,3
        # result= [1,2,8,48]
        for i in range(1,len(nums)): #2
            prefix[i] = nums[i-1] * prefix[i-1]
        
        #  suffix
        for i in range(len(nums)-2 , -1 ,-1):
            postfix[i] = nums[i+1] * postfix[i+1]
        
        for i in range(0,len(nums)):
            result[i] = prefix[i] * postfix[i]
        return result


        # calculate the postfix
        # nums =  [1,2,4,6]
        # postfix=[1,1,1,1]
        # result= [48,48,24,6]



        # in the result array put and multiply them and return the result


          
        