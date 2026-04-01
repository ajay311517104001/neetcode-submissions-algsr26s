class Solution:
    # memo approach
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            res = float('+inf')
            for c in coins:
                if amount - c>=0:
                   res = min(res,dfs(amount - c)+1)
            
            memo[amount] =  res

            return res
            


        val = dfs(amount)

        return -1 if val == float('+inf') else val
        