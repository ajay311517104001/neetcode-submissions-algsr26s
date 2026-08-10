class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        space1 = [0]*26
        space2 = [0]*26

        for i in range(len(s1)):
            space1[ord(s1[i]) - ord("a")]+=1
            space2[ord(s2[i]) - ord("a")]+=1

        l = 0
        for r in range(len(s1) , len(s2)):
            if space1 == space2:
                return True

            space2[ord(s2[r]) - ord("a")]+=1
            space2[ord(s2[l]) - ord("a")]-=1
            l+=1
        return space1 == space2
