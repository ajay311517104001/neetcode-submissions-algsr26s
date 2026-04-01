class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        subset , result = [], []
        # pass the index or the n to the helper starts from 1
        # return result set

        def dfs(i):
            # basecase
            if len(subset) == k:
                result.append(subset.copy())
                return
            if i>n:
                return
            
            subset.append(i)
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(1)
        return result