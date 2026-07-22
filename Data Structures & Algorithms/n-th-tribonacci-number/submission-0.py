class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        def solve(i):

            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1
            if i in cache:
                return cache[i]

            cache[i] = solve(i-1) + solve(i-2) + solve(i-3)
            return cache[i]
        
        return solve(n)