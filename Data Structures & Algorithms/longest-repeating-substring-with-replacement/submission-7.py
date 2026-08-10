class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxi = float("-inf")
        space = [0]*26
        while r < len(s):
            space[ord(s[r]) - ord("A")]+=1
            while (r-l+1) - max(space) > k:
                space[ord(s[l]) - ord("A")]-=1
                l+=1
            maxi = max(maxi , r-l+1)
            r+=1
        return maxi 
        