class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # declare the global max area
        #  [1,3,7]
    #    l=1      i r=3
        # maxArea = 0 # 3 6 7
        # # iterate all the element
        # for i in range(len(heights)):
        # # for each element find the right most location where it should be less than the current
        #     rightMost = i+1
        #     while rightMost < len(heights) and heights[rightMost] >= heights[i]:
        #         rightMost+=1
        # # for the same elment find the left most element which is less than the current
        #     leftMost = i-1
        #     while leftMost >=0 and heights[leftMost] >= heights[i]:
        #         leftMost-=1
        # #  update the max area
        #     maxArea = max(maxArea, heights[i]* (((rightMost-1) - (leftMost+1))+1))
        # # return the max area 
        # return maxArea

        # The optimal solution would be, Instead of the while we will be using the stack
        # find the array of previos smaller element using stack
        # [7,1,7,2,2,4]
                    #  i
        # [-1,-1,1,1,1,2]
        # stack=[1,4]
        # create an array of negative 1 - question why not zeros?
        leftMost= [-1] * len(heights)
        #  iterate thru the elements
        stack=[]
        for i in range(len(heights)):
        # push element to the stack
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)
        print(leftMost)
        #  condition when the incoming elmement is less than the stak top
        #  remove all elements from stack till you find the curr element
        # remove the element if stack top is less than current
        # append the current

        # find the array of next smaller element
        #  0 ,1, 2  3  4  5
        # [7, 1, 7, 2, 2, 4]
                #  i
        # [1,-1,2,-1,-1,-1]
        # stack=[3]
        stack=[]
        rightMost = [len(heights)]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        print(rightMost)


        # find the area using the those to array
        maxArea = 0
        for i in range(len(heights)):
            left = leftMost[i]+1
            right = rightMost[i]-1
            maxArea = max(maxArea, heights[i]*(right - left + 1))
        return maxArea

