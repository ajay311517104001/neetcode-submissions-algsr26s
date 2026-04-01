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
        #  Time complexity - O(n2) and space complexity - O(n)
        # while '()' in s or '[]' in s or '{}' in s: # O(n)
        #     s = s.replace('()', '')  #O(N)
        #     s = s.replace('[]','') # replace internally uses O(n) space to store the element
        #     s = s.replace('{}','')
        # return s == ''


        #  create a stack
        stack = []
        # iterate and push only the opening bracket
        close_bracket = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        for i in range(len(s)):
        #  if close bracket arrives check the top of the stack if its is the same openeing bracket
            if not close_bracket.get(s[i],0): 
                stack.append(s[i])
            else:
                if stack and stack[-1] == close_bracket.get(s[i]) :
                    stack.pop()
                else:
                    return False
                
        # pop the top of the stack
        return True if stack == [] else False
        # if the top is not matching return false
        # if stack is empty return the true


