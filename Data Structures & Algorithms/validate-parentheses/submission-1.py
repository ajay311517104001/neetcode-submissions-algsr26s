class Solution:
    def isValid(self, s: str) -> bool:
        #  it can implement with two pointers
        #  add left to its 0 th index and right to the last index
        # L,R = 0 , len(s)-1
        # hmap={
        #     '{':'}',
        #     '[':']',
        #     '(':')'
        # }
        # # s="()[]{}" Two pointer can solve this problem partially
        # #  till left < right
        # while L<R:
        # #  if left != right
        #     print(s[L],s[R])
        #     if hmap[s[L]]!=s[R]:
        # #  return false
        #         return False
        #     L+=1
        #     R-=1
        # # after loop return true
        # return True

        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '')
            s = s.replace('[]','')
            s = s.replace('{}','')
        return s == ''