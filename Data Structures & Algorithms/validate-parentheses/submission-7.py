class Solution:
    def isValid(self, s: str) -> bool:
        # openToclose = { '(':')' ,
        #                 '{': '}',
        #                 '[': ']'}
        # This will only work for palidrome
        # L =0
        # R = len(s)-1
        # while L<R:
        #     if openToclose[s[L]] != s[R]:
        #         return False
        #     L+=1
        #     R-=1
        # return True

        closeToopen = { ')':'(' ,
                        '}': '{' ,
                        ']': '['}

        stack = []

        for i in s:
            if i in closeToopen:
                if stack and stack[-1] == closeToopen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False


