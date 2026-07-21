class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for r in range(0,n):
            for c in range(r , n):
                matrix[r][c] , matrix[c][r] = matrix[c][r] , matrix[r][c]
        
        for i in range(n):
            matrix[i].reverse()
        