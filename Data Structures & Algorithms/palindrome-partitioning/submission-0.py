class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        unit =[]
        def dfs(i):
            # basecase
            # check if the index reaches the end of the string
            if i >= len(s):
                result.append(unit.copy())
                return
            # then add

            # iterate thru start to end of the string
            for j in range(i,len(s)): # 0
            # check if my start is a valid palindrome
                if isPali(i,j):
                    unit.append(s[i:j+1])
                    dfs(j+1)
                    unit.pop() # pop is happening to backtrack the depth and make the array empty
        
        

            # add that to the list
            # send the index after partition to process the rest of the string
            # why pop?


        def isPali(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l , r = l+1 ,r-1
            return True


        dfs(0)


        return result