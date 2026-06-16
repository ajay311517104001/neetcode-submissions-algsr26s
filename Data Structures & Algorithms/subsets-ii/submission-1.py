class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #         2^n   →  total number of subsets in the recursion tree (each element: include or exclude)
# n     →  cost to copy each subset via path[:]

# Total = O(n × 2^n)
        
#         Auxiliary space (recursion call stack + path during execution):
#   O(n)  — max recursion depth is n (bounded by array length),
#           only one path exists on the stack at any moment

# Output space (res storing all subsets):
#   O(n × 2^n)  — up to 2^n subsets stored, each up to size n
        nums.sort()

        res = []
        path = []


        def solve(start ,path):
            res.append(path[:])

            for i in range(start ,len(nums)):
                if i > start and nums[i-1] == nums[i]:
                    continue
                path.append(nums[i])
                solve( i+1, path)
                path.pop()
        solve(0,path)
        return res