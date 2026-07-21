class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # get the row datas and column datas
        ROW , COL = len(matrix) , len(matrix[0])

        # iterate the grid and update the top row and left column
        rowZero = False

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
                        
        print("update the marks ",matrix)
        
        #  mark 0 to the inner grid
        for r in range(1,ROW):
            for c in range(1,COL):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        print("update the body", matrix)
        
        if matrix[0][0] == 0:
            for r in range(ROW):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COL):
                matrix[0][c] = 0



        