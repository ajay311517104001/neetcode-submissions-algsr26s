class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        hmap = {len(s): True}
        def dfs(i):
            if i in hmap:
                return hmap[i]
            
            for w in wordDict:
                if  i+len(w) <= len(s) and s[i:i+len(w)] == w :
                    if dfs(i+len(w)):
                        hmap[i] = True
                        return True
            
            hmap[i] = False
            return False
        return dfs(0)
