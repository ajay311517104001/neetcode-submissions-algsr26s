"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def solve(r , c , size):
            # check if the entire grid has same values
            firstVal = grid[r][c]
            sameVal = True

            for i in range(r , r+size):
                for j in range(c , c+size):
                    if firstVal != grid[i][j]:
                        sameVal = False
                        break
                if not sameVal:
                    break


            # if yes return the node
            if sameVal:
                return Node(bool(firstVal) , True)

            # else go to next level and do the same thing
            half = size // 2
            topleft = solve(r , c , half)
            topright= solve(r , c + half , half)
            bottomleft = solve(r + half , c , half)
            bottomright = solve(r+half , c+half , half)

            # return the result node
            return Node(bool(firstVal) , False , topleft , topright , bottomleft , bottomright)
        
        return solve(0,0,len(grid))






        