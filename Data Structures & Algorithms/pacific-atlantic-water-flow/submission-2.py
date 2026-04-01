class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return heights
        
        ROWS , COLUMNS = len(heights) , len(heights[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        pacific = False
        atlantic = False
        visited = set()
        def dfs(r,c , preVal):
            nonlocal pacific , atlantic
            if pacific and atlantic:
                return 
            if( r < 0 or c < 0):
                pacific = True
                return
            if( r >= ROWS or c>= COLUMNS):
                atlantic = True
                return
            if heights[r][c] > preVal:
                return
            if (r,c) in visited:
                return

            visited.add((r,c))
            preVal = heights[r][c]
            for dr , dc in directions:
                nrd = r+dr
                ncd = c+dc
                dfs(nrd,ncd , preVal)
            visited.remove((r,c))
            
        
        result = []
        for r in range(ROWS):
            for c in range(COLUMNS):
                pacific = False
                atlantic = False
                dfs(r,c , heights[r][c])
                if pacific and atlantic:
                    result.append([r,c])
        return result


        