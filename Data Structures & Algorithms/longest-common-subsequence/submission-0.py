class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def solve(i,j):
            if len(text1) == i or len(text2) ==  j:
                return 0 

            if (i,j) in cache:
                return cache[(i,j)]

            if text1[i] == text2[j]:
                 cache[(i,j)] =  1 + solve(i+1 , j+1)
                 return  cache[(i,j)]
            else:
                cache[(i,j)] = max(solve(i+1 , j), solve(i,j+1))
                return  cache[(i,j)]

        return solve(0,0) 

