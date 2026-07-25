class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []


        def solve(path , hmap):
            if len(path) == len(nums):
                res.append(path[:])
                return 
            
            for n in hmap:
                if n in hmap and hmap[n]:
                    path.append(n)
                    hmap[n]-=1
                    solve(path , hmap)
                    hmap[n]+=1
                    path.pop()
        
        

        hmap = {}

        for n in nums:
            hmap[n] = hmap.get(n , 0) +1
        solve([], hmap)
        return list(res)
            
