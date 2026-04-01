class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(amt , cache):
            if amt == 0:
                return 0
            if amt in cache:
                return cache[amt]

            res = float('+inf')
            for c in coins:
                if amt - c>=0:
                    res = min(res, dfs(amt-c , cache) +1)
                    cache[amt] = res
            return res

        result = dfs(amount , {})

        return result if result!= float('+inf') else -1
        