class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        space = set() 
        length = 0
        while r < len(s):
            while s[r] in space:
                space.remove(s[l])
                l+=1
            space.add(s[r])
            length = max(length , r - l + 1)
     
                

            r+=1
        return length
