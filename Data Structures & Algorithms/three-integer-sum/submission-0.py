class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # conditions
        # i,j,k all are unique
        #  output should not contains duplicates
        # I can return the ouput triplets in any order
        #  The sum i need to get is 0 when i add nums[i] + nums[j] + nums[k] == 0
        #  need to return as numbers not as index
        # Rough work
        #  [-1,0,1,2,-1,-4]
        #      i j    k

        # -1 + 0 + 1 = 0 add to array
        #  check if it exists in the array
        # -1 + 0 + 2 = 1
        # -1 + 0 -1 = -2
        # -1 + 0 -4 = -5

        # -1 + 1 + 2 = 2
        # -1+1-1 = 1
        # -1 + 1 -4 = -4
        # TC- O(n3) + nlogn = O(n3) , space O(n) n-> is the number of triplets
        result = set()
        nums.sort()
        #  sort to handle the duplicates
        for i in range(0,len(nums)-2):
            for j in range(i+1 , len(nums)-1):
                for k in range(j+1 , len(nums)):
                    # check if the triplets making zero
                    if nums[i] + nums[j] + nums[k] == 0 :
                    #  if yes check tat triplet exists in the result
                        result.add(tuple([nums[i],nums[j],nums[k]]))
                    # if not update the result
        return list(result)




