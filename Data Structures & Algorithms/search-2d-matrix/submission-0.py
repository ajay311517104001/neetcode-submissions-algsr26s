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
        for i , row in enumerate(matrix):
        #  for each row perfrom binary search
        #  initialize left pointer (I,0)
            left =0
            # initlialze rirght pointer which is the (I,len(row) -1)
            right = len(row)-1
            while left <= right:
            # while L<=R:
            #  find the mid by adding left and right pointer /2
                mid = (left+right)//2
            # if the target > mid ele
                if target > matrix[i][mid]:
            # left = mid +1
                    left = mid+1
            # if the target < mid ele
                elif target < matrix[i][mid]:
            # right = mid -1
                    right = mid-1
            # else
                else:
                    return True
            # return bool
        return False
        # return the boolean