class Solution:
    def trap(self, height: List[int]) -> int:
        #  partially worked solution - made form scratch
        # # [0,2,0,3,1,0,1,3,2,1]
        #                 #  l   r
        # # l =0
        # l=0
        # total_quantity = 0
        # r=0
        # # outer loop till r< len of the array
        # while r < len(height):
        # # iterate thru the array till you find a number greater than 0 that is l
        #     count=0
        #     while height[l]  <= 0:
        #         l+=1
        #     # the next element is r
        #     r=l+1
        #     # iterate the right till you find a value which is equal or greater than my l and keep count
        #     while r < len(height) and height[r] < height[l]:
        #         r+=1
        #         count+=1
        #     # take that L and R and get its min
        #     # iterate the sub array and subtract with minand add that to total quantity
        #     if r<len(height) :
        #         lim =min(height[l],height[r])
        #         for i in range(count):
        #             total_quantity+= lim - height[l+1+i]

        #     # l will be my right 
        #         l=r
        
        # #  right will be right plus 1
        # # return the total quantity
        # return total_quantity
        total_sum = 0
        #  solving it using the prefix sums and postfix sums
        leftMax = [0]*len(height)
        rightMax = [0]*len(height)
        #  calculate the left max
        lmax = 0
        # [0,2,0,3,1,0,1,3,2,1]
        # [0,0,0,0,0,0,0,0,0,0] 
        for i in range(0,len(height)-1):
            lmax = max(lmax,height[i])
            leftMax[i+1] = lmax
        #  calculate the right max
        rmax = 0
        for i in range(len(height)-1 ,0,-1):
            rmax = max(rmax,height[i])
            rightMax[i-1] = rmax
        print(leftMax)
        print(rightMax)
        # calculate the result
        for i in range(len(height)):
            total_sum+= min(leftMax[i], rightMax[i]) - height[i] if (min(leftMax[i], rightMax[i]) - height[i]) >0 else 0
        #  return the sum
        return total_sum



