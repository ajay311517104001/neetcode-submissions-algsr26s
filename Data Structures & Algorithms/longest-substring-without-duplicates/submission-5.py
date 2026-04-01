class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        l =0
        hm = set()
        for r in range(0,len(s)):
            while s[r] in hm:
                hm.remove(s[l])
                l+=1
            hm.add(s[r])
            maxi = max(maxi , r-l+1)
        return maxi
