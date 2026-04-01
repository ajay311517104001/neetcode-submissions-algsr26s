class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # what could be my naive solution
        #  try all combinations and check the string is valid?
        def isValid(stack):
            # string should have 3 open and 3 close bracket
            # It should always start with open bracket
            # return True
            balance =0
            for i in stack:
                if i == '(':
                    balance+=1
                if i == ')':
                    balance-=1
                if balance == -1:
                    return False
            
            return balance==0 


        result = []
        stack = []
        def dfs(stack):
            if len(stack) == 2*n and isValid(stack):
                result.append("".join(stack))
                return 
            if len(stack) > 2*n:
                return

            stack.append('(')
            dfs(stack)
            if stack:
                stack.pop()
            
            stack.append(')')
            dfs(stack)
            if stack:
                stack.pop()

        if n==0:
            return result
        dfs(stack)

        return result