class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # def dfs(amount , cache):
        #     if amount == 0:
        #         return 0
        #     if amount in cache:
        #         return cache[amount]

        #     mini = float("inf")
        #     for c in coins:
        #         if amount - c>=0:
        #             mini = min(mini , dfs(amount - c, cache)+1)
        #     cache[amount] = mini
        #     return mini

        # res = dfs(amount , {})
        dp = [float("+inf")] * (amount+1)
        dp[0] = 0
        i =1
        while i <= amount:

            for c in coins:
                if i - c >=0:
                    dp[i] = min(dp[i] , dp[i-c]+1)
            i+=1
        return -1 if dp[amount] == float("+inf") else  dp[amount]
        # dp = [float('+inf')] * (amount+1)
        # dp[0] =  0


        # for i in range(1,amount+1):

        #     for c in coins:
        #         if i-c >=0:
        #             dp[i] = min(dp[i] , dp[i-c]+1)

        # return dp[-1] if dp[-1]!= float("+inf") else -1
        