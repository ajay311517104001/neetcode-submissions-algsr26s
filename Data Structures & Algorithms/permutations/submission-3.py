class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []
        def solve(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                solve(path)
                path.pop()
        solve(path)

        return res