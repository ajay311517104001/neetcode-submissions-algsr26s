class Solution:
    # IMPLEMENTED WITH THE BFS APPROACH
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS IMPLEMENTATION
        if not grid:
            return 0
        ROWS , COLUMNS = len(grid) , len(grid[0])
        total_island = 0
        visited=set()
        enque = collections.deque()
       
        def BFS(r,c):
            direction = [(0,-1), (0,1) , (1,0),(-1,0)]
            enque.append((r,c))
            visited.add((r,c))
            while enque:
                r,c = enque.popleft()
                for dr,dc in direction:
                    nrd = r+dr
                    ncd = c+dc
                    if(min(nrd,ncd)<0 or nrd == ROWS or ncd == COLUMNS or grid[nrd][ncd]=='0' or (nrd,ncd) in visited):
                        continue
                    enque.append((nrd,ncd))
                    visited.add((nrd,ncd))
            return


            
            
            


        for r in range(ROWS):
            for c in range(COLUMNS):
                # check if the element is 1 and it not visited
                if grid[r][c] == '1' and (r,c) not in visited:
                    BFS(r,c)
                    total_island+=1
        return total_island
