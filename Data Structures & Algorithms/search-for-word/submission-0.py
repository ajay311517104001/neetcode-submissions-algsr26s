class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = set()
        ROWS , COLUMNS = len(board) , len(board[0])
        def dfs(i , j , ind):
        #    basecase
            if ind == len(word):
                return True
            if (i <0 or j<0 or i >= ROWS or j >= COLUMNS or board[i][j].lower()!=word[ind].lower() or (i,j) in path ):
                return False
            
            
            # backtracking
            # It is a valid index
            path.add((i,j))
            neighbours = (dfs(i-1 , j , ind+1) or
                         dfs(i+1 , j , ind+1) or
                         dfs(i , j-1 , ind+1) or
                         dfs(i , j+1 , ind+1))
            path.remove((i,j))
            return neighbours



        for i in range(ROWS):
            for j in range(COLUMNS):
                if dfs(i,j,0):
                    return True
        return False