class Solution:
    def tribonacci(self, n: int) -> int:
        # cache = {}
        # def solve(i):

        #     if i == 0:
        #         return 0
        #     if i == 1 or i == 2:
        #         return 1
        #     if i in cache:
        #         return cache[i]

        #     cache[i] = solve(i-1) + solve(i-2) + solve(i-3)
        #     return cache[i]
        
        # return solve(n)
        if n == 0 :
            return 0
        if n == 1 or n == 2:
            return 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]