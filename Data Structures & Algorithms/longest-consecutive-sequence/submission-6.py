class Solution:
    # optimal solution
    def longestConsecutive(self, nums: List[int]) -> int:

        # DRY RUN
        # [5,3,1,2,6]
        #    0,1,2,3,4
        #        i


        num_set = set()
        # add all the elements to the hashset
        for i in nums:
            num_set.add(i)
        sequence = 0
        result = 0
        # itereate thru the elemnts 
        for i in range(len(nums)):
        # for each and every element subtract and check in the set
        #  if the set does not contain any values means that is the start of the sequence
            if nums[i]-1 not in num_set:
        #  start there keep in increment and check the result set if that exits
        #  if not that's where our sequence breaks
                seq = nums[i]
                while seq in num_set:
                    sequence+=1
                    seq+=1
                result = max(result , sequence)
                sequence =0
        # update the result with the max sequence
        # return the max
        return result

        # TimeComplexity: O(N) + O(N) -> O(n)
        # Space complexity : O(N)