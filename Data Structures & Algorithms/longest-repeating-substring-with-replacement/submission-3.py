class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        maxi = 0
        res = 0
        for r in range(0,len(s)):
            count[s[r]] = count.get(s[r] , 0)+1
            
            #condition to check if we have enough provision to maintain if not chop form front 
            maxi = max(maxi , count[s[r]])

            while r-l+1 - maxi > k:
                count[s[l]]-=1
                l+=1
            res = max(r-l+1 , res)
        return res

