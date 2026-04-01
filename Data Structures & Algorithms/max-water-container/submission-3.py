class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force approach - tc-O(n2) SC = O(1) 
        #  setmav value
        # [1,7,2,5,4,7,3,6]
        #  0 1 2 3 4 5 6 7
        # maxValue = 0
        # #  iterate the i 
        # for i in range(len(heights)-1):
        # #  iterate the j +1
        #     for j in range(i+1 , len(heights)):
        # #  find the min * substracet the indices
        #         total_quantity = min(heights[i], heights[j]) * (j-i)
        # #  setmax if its greater
        #         maxValue = max(maxValue,total_quantity)
        # # return setmax
        # return maxValue

        # optimized approach - How we gonna imporve the time complexity?
        # initialize left and right pointer
        # [1,7,2,5,4,7,3,6]
        #  0 1 2 3 4 5 6 7
            #  l           r
        l,r = 0 , len(heights)-1
        # max vlaue
        maxValue = 0
        # iterate till R < len(array)
        while l<r:
        # total_quantity = min(heights[left], heights[right]) * (left-right)
            total_quantity = min(heights[l], heights[r]) * (r-l)
        # setmax
            maxValue = max(maxValue , total_quantity)
        # if L<R
            if heights[l] < heights[r]:
        #    L=R
           
                l+=1
        #  R+1
            else:
        # ELSE
                r-=1
        # R+1
        return maxValue


        