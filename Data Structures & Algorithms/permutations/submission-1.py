class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
    
        def helper(i):
        
            if i == len(nums):
                return [[]]

            result = []
            per = helper(i+1)
            for p in per:
                for k in range(len(p)+1):
                    copy_p = p.copy()
                    copy_p.insert(k,nums[i])
                    result.append(copy_p)
            return result

        return helper(0)
