class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        hmap={
            '2': 'abc',
            '3':'def',
            '4': 'ghi',
            '5' :'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        result = []
        def dfs(index , path):
            # if the index reached the word last length add it to the result
            # return
            if index == len(digits):
                result.append("".join(path))
                return

            for char in hmap[digits[index]]:
                path.append(char)
                dfs(index+1 , path)
                path.pop()

        dfs(0,[])

        return result