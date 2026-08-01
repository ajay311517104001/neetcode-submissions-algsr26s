class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # need to calculate the global mini

        res = float("inf")
        cache = {}
        def solve(i , count):
            nonlocal res , cache
            if i == len(s):
                res =  min(count , res)
                return 
            
            if i in cache and cache[i] <= count:
                return 
            cache[i] = count

            
            for w in dictionary:
                
                if s[i:i+len(w)] == w:
                    print(s[i:i+len(w)], w)
                    solve(i+ len(w) , count)
            
            if len(s) > i:
                solve(i+1 , count+1)
            
            return 
        solve(0, 0)
        return res 