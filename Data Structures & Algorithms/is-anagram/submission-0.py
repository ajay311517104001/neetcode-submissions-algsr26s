class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute force approach
        #  we can sort both and check if both strings are equal
        # 0(n log n)
        # return sorted(s) == sorted(t)

        # Optimized approach - dict  - 0(n)
        smap ={}
        tmap = {}
        #  if both strings are not equal return false 0(n)
        if len(s) != len(t):
            return False
        #  run thru the loop with lenght of the string 0(n)
        for i in range(0, len(s)):
        #     populate the smap
            if smap.get(s[i]):
                smap[s[i]]+=1
            else:
                smap[s[i]]=1
        #     populate the tmap
            if tmap.get(t[i]):
                tmap[t[i]]+=1
            else:
                tmap[t[i]]=1
        # if both map are equal return true , else false
        return smap == tmap
        