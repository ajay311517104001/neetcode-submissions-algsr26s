class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sorted_arr = sorted(nums)
        # brute force solution
        #  sort the array which is O(nlogn) space complexity - 0(n)
        # [100,4,200,1,3,2]
        # [1,2,3,4,100,200]
        # [0,3,7,2,5,8,4,6,0,1]
        # [0,0,1,2,3,4,5,6,7,8]
        # longest_sequence = 0 
        # curr = 1
        # #  iterate thru the element
        # if len(nums) == 0:
        #     return 0
        # for i in range(0,len(nums)-1):
        # #  check if the first element is +1 of the second element
        #     if sorted_arr[i+1] == sorted_arr[i]+1:
        #     #  if yes
        #         #  increment the curr
        #         curr+=1 #4
        #     elif sorted_arr[i+1] == sorted_arr[i]:
        #         continue
        #     #  if no
        #     else:
            
        #         #  if curr > longest_suquence
        #         if curr> longest_sequence:
        #             longest_sequence = curr
        #         curr=1
        # return longest_sequence if longest_sequence > curr else curr
        # This logic is not working
        # [9,1,4,7,3,-1,0,5,8,-1,6]
        # [-1,-1,0,1,3,4,5,6,7,8,9]
        # [1,0,1,2]
        # [0,1,1,2]

        # Brute force approach without sorting
        # [100,4,200,1,3,2]
        #  set removes duplicate and lookup in set is O(1)
        #  take one element from array
        store =set(nums)
        res = 0
        for num in nums:
        # add +1 to it and check if that exists in the set
        # if not reset the streak
            curr , streak = num , 0
        #  if exists maintain streak
            while curr in store:
                curr+=1
                streak+=1
            if streak > res:
                res = streak
        
        # if streak>res res = streak
        # return res
        return res



        