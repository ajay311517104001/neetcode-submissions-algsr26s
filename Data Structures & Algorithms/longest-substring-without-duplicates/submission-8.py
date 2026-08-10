class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        maxi = float("-inf")
        space = set()
        while r < len(s):
            while s[r] in space:
                space.remove(s[l])
                l+=1
            
            space.add(s[r])
            maxi = max( maxi, r-l+1)
            r+=1
        return maxi if maxi != float("-inf") else 0 
































        # maxi = 0
        # l =0
        # hm = set()
        # for r in range(0,len(s)):
        #     while s[r] in hm:
        #         hm.remove(s[l])
        #         l+=1
        #     hm.add(s[r])
        #     maxi = max(maxi , r-l+1)
        # return maxi
