class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Naive approach 
        # Time and space complexity - 4 move - 4 add = 8 <= 2(n) -> O(2n) -> O(n)
        # return nums+nums

        # create new array -> ans of size 2(n)
        ans = [0]  * (2 * len(nums))
        print(ans)
        # [1,2] -> [1,2,1,2]
        #    i     ==     i
        # ans[3] == nums [1]
        #  2  == 2
        for i in range(0,len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]
        return ans
