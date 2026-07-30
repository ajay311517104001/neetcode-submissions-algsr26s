class Solution:
    def numWays(self, n: int, k: int) -> int:
        cache = {}
        def solve(i):
            nonlocal cache
            if i == 1:
                return k
            if i == 2:
                return k*k
            
            if i in cache:
                return cache[i]
            
            cache[i] = (k-1) * (solve(i-1) + solve(i-2))

            return cache[i]
        
        return solve(n)
        



