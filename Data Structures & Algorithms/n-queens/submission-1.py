class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def isValid(board , row):
            pass

        positiveDiag = set()
        negativeDiag = set()
        vertical = set()
        board = []
        def dfs(r ):
            # add when the position exists the board size
            if r == n:
            # add the result 
                result.append(board.copy())
                return
            # return to explore other options
            
            for col in range(n):
            # add the queen to the board based on the incoming position and iterate thru the rest of the row
                if r - col in negativeDiag  or r + col in positiveDiag or col in vertical:
                    continue

                row = ['.']*n
                row[col] ="Q"
                # if isValid(board , row):
                negativeDiag.add(r-col)
                positiveDiag.add(r+col)
                vertical.add(col)
                board.append( ''.join(row))
                dfs(r+1)
                board.pop()
                negativeDiag.remove(r-col)
                positiveDiag.remove(r+col)
                vertical.remove(col)

            # check if the added queen violates the condition
            # if yes pop the last row and the iteration handles the rest of the rows


        
        dfs(0 )

        return result