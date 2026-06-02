class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        arr = [0]*26
        length = 0
        for r , c in enumerate(s):
            arr[ord(s[r]) - ord("A")]+=1
            while  (r -l+1) - max(arr) > k:
                # remove from left
                arr[ord(s[l]) - ord("A")]-=1
                l+=1
            length = max(length , r-l+1)
        return length
            

               