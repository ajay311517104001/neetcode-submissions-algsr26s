class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # add both array
        #  sort them
        # check if the length is even or odd
        # if odd return the middle value
        #  if even mid and next value to mid divide it by 2
        result = nums1+nums2
        result.sort()
        size = len(result)
        l=0
        r = len(result) -1
        mid = (l+r)//2
        if result:
            if size%2 == 1:
                return result[mid]
            else:
                return (result[mid] + result[mid+1])/2

        