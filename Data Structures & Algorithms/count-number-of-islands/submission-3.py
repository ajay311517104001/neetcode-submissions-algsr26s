class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        visited = set()

        def BFS(k,l):
            # It should explore all the connected island mark them visited
            enque = deque()
            enque.append((k,l))
            visited.add((k,l))
            directions = [(0,-1) , (0,1) , (1,0) ,(-1,0)]
            while enque:
                i,j = enque.popleft()
                for dr , dc in directions:
                    ndr = i+dr
                    ndc = j+dc
                    if min(ndr,ndc) <0 or ndr >= ROWS or ndc >= COLUMNS or (ndr,ndc)  in visited or grid[ndr][ndc]== '0':
                        continue
                    visited.add((ndr,ndc))
                    enque.append((ndr,ndc))


            

        # iterate each and evey cell position and call bfs if it is 1
        total_island = 0
        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == '1' and (i,j) not in visited:
                    BFS(i,j)
                    total_island+=1
        return total_island

        