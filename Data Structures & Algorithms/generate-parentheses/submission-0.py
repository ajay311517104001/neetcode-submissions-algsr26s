class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # choice - i have n to create valid combination of parentheses
        # basecase - if my string length is 6 i will stop and add it to the list
        # constraint - no duplicates and no non well formed string and string greater than 2n
        # backtracking : explore the left branch when open < n and explore the right branch when close < open


        result = []


        def dfs(str_ , open_ , close):
            # basecase
            if len(str_) == 2*n:
                result.append(str_)
                return
            if open_ < n:
                dfs(str_+'(' , open_ +1 , close)
            if close < open_:
                dfs(str_ + ')' , open_ , close + 1)

        dfs('' , 0 , 0)

        return result
        