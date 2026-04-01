class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        grid = [ [False]*n for i in range(n)]
        max_len = float('-inf')
        start_index = 0
        end_index = 0
        for i in range(n-1 , -1 ,-1):
            for j in range(i , n):
                if s[i] == s[j] and ( j-i <=2 or grid[i+1][j-1]):
                    grid[i][j] = True
                    if max_len < (j-i+1):
                        max_len = j-i+1
                        start_index = i
                        end_index = j
        

        return s[start_index:end_index+1]
