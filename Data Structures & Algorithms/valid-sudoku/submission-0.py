class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # first need to check if the rows has any duplicate values. if yes return false
    #  we'll use hashset
   
        for row in range(9):
            rmap = set()
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in rmap:
                    return False
                rmap.add(board[row][col])
                
        # second need to check if the col has duplicate values if yes return false
        for row in range(9):
            cmap = set()
            for col in range(9):
                if board[col][row] =='.':
                    continue
                if board[col][row] in cmap:
                    return False
                cmap.add(board[col][row])

        # check squares if it has any duplicate values in it
        for square in range(9):
            square_set = set()
            for i in range(3):
                for j in range(3):
                    row = (square%3)*3+ i
                    col = (square//3)*3+j
                    if  board[row][col] == '.':
                        continue
                    if board[row][col] in square_set:
                        return False
                    square_set.add(board[row][col])
        
        return True 




