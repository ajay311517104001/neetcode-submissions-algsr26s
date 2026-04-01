class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # iterate thru the elements
        # while incoming elmeent in dict
        # remove the element from the dict
        # add it ot the dict and update the global
        l=0
        hmap =set()
        maxi = 0
        for r in range(0,len(s)):
            while s[r] in hmap:
                hmap.remove(s[l])
                l+=1
            hmap.add(s[r])
            maxi =max(maxi , r-l+1)
        return maxi

        