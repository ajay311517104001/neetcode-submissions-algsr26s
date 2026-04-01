class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # what i would do is that instead of going thru all the land cell and check the min distance between start to the treasure
        # The Time Complexity would be much higher -> O(n.m * m.n)

        # we can proceed with an optimal solution where we can start from all the gates avialable for each and every gate
        # using bfs we explore the cells by layer each layer defines the distance between the treausre and the cell itself
        # for the second gate we can use the minimum to modify the grid

        if not grid:
            return grid

        ROWS , COLUMNS = len(grid), len(grid[0])

        # collect the all possible gates
        gates = set()
        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 0:
                    gates.add((i,j))
        # For each and every gate we need to traverse and update the distance in the grid by modifying them

        enque = collections.deque()
        visited = set()
        directions = [ [0,-1],[0,1],[1,0],[-1,0]]
        
        for i,j in gates:
            enque.append((i,j))
            visited.add((i,j))
            layer=0
            while enque:
                layer+=1
                for _ in range(len(enque)):
                    r,c = enque.popleft()
                    visited.add((r,c))
                    for dr , dc in directions:
                        nrd = r+dr
                        ncd = c+dc
                        if (min(nrd,ncd)<0 or nrd >=ROWS or ncd >=COLUMNS or grid[nrd][ncd]== -1 or (nrd,ncd) in visited):
                            continue
                        grid[nrd][ncd] = min(grid[nrd][ncd],layer)
                        enque.append((nrd,ncd))
            visited = set()
        return 


        