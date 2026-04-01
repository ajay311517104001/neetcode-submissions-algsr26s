class Solution:
    def numDecodings(self, s: str) -> int:
        
        # '1 2 1 2 1' -1
        # '1 2 1  21' -1
        # '1 2 12 1' - 1
        # '1 21 2 1' - 1
        # '1 21 21' - 1
        # '12 1 2 1' - 1
        # '12 1 21' - 1
        # '12 12 1' - 1

        # i   
        #01234

        # '1202' 
        # #0123

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            res = dfs(i+1)
            if i < len(s)-1:
                if 10 <= int(s[i:i+2]) <= 26:
                    res+=dfs(i+2)

            

            return res
             
        
        return dfs(0)
