class Solution:
    # DFS Implementation
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_land = 0
        if not grid:
            return max_land

        ROWS , COLUMNS = len(grid) , len(grid[0])
        # dfs to explore the lands
        directions = [[1,0] , [-1,0] , [0,1] , [0,-1]]
        def dfs(r,c):
            if (min(r,c)<0 or r == ROWS or c == COLUMNS or grid[r][c]== 0):
                return 0
            # area=1
            # visited.add((r,c))
            grid[r][c] =0
            # for dr , dc in directions:
            #     ndr , ndc = r+dr , c+dc
            #     area+=dfs(ndr , ndc)
            return (1+ dfs(r+1,c) + dfs(r-1,c)+ dfs(r,c+1)+ dfs(r,c-1))
            # return area

        # iteratively visit all the index and look for only the land 
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] ==1:
                    max_land =max(max_land,dfs(r,c))
                    
        return max_land


        