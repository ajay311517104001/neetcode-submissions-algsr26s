class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def solve(start , path , curr):
            if curr == target:
                res.append(path[:])
                return 
            
            if curr > target:
                return 

            
            for i in range(start , len(candidates)):
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                path.append(candidates[i])
                solve(i+1 ,path , curr + candidates[i])
                path.pop()
        solve(0,path , 0)
        return res
        