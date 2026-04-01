class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # declare the global max area
        #  [1,3,7]
    #    l=1      i r=3
        maxArea = 0 # 3 6 7
        # iterate all the element
        for i in range(len(heights)):
        # for each element find the right most location where it should be less than the current
            rightMost = i+1
            while rightMost < len(heights) and heights[rightMost] >= heights[i]:
                rightMost+=1
        # for the same elment find the left most element which is less than the current
            leftMost = i-1
            while leftMost >=0 and heights[leftMost] >= heights[i]:
                leftMost-=1
        #  update the max area
            maxArea = max(maxArea, heights[i]* (((rightMost-1) - (leftMost+1))+1))
        # return the max area 
        return maxArea