class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute force soulution would be
        # iterate the matrix 
        # for row in matrix:
        # #  for each index perfrom scan the elements for target value
        #     for element in row:
        #         if element == target:
        #             return True
        # return False
        # if target value is determied return the value
        # T.c O(n2) SC 

        # Optimized solution - reduce the time to find the target element
        #  iterate the matrix
        #  [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
        #            0           1             2
        # # TC - >m.Logn S.C -> O(1)
        # for i , row in enumerate(matrix):
        # #  for each row perfrom binary search
        # #  initialize left pointer (I,0)
        #     left =0
        #     # initlialze rirght pointer which is the (I,len(row) -1)
        #     right = len(row)-1
        #     while left <= right:
        #     # while L<=R:
        #     #  find the mid by adding left and right pointer /2
        #         mid = (left+right)//2
        #     # if the target > mid ele
        #         if target > matrix[i][mid]:
        #     # left = mid +1
        #             left = mid+1
        #     # if the target < mid ele
        #         elif target < matrix[i][mid]:
        #     # right = mid -1
        #             right = mid-1
        #     # else
        #         else:
        #             return True
        #     # return bool
        # return False
        # return the boolean

        # Optimal approach instead of checking in all the rows we figure out which row does the tartget value may reicide and perfrom binray search on that row
        #  find the mid for the matrix 
        # [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
            #    0           1             2
        L=0
        R = len(matrix) -1
        while L<=R:
            MID = (L+R)//2
        #  if target < mid row [1]:
            if target < matrix[MID][0]:
            # right -=1
                R=MID-1
        # elif target > mid row[len(array)-1]
            elif target > matrix[MID][len(matrix[MID])-1]:
            #  left+=1
                L= MID+1
        # check if left < target and right is > target
            else:
                left = 0
                right = len(matrix[MID])-1
                while left <= right:
                    mid = (left+right)//2
                    if target > matrix[MID][mid]:
                        left= mid+1
                    elif target < matrix[MID][mid]:
                        right = mid-1
                    else:
                        return True
                break
        #  perfrom binary search 
        return False
       