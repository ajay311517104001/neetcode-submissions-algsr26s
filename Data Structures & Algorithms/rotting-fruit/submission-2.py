class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLUMNS = len(grid) , len(grid[0])
        enque = collections.deque()

        
        # collecting the rotton oranges spots
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 2:
                    enque.append((r,c))
        # check if there are no rotton orange so it is -1 as per the rule
        if not enque:
            for r in range(ROWS):
                for c in range(COLUMNS):
                    if grid[r][c] == 1:
                        return -1
            return 0

        directions = [ [0,-1],[0,1],[1,0] ,[-1,0]]
        minute = -1
        # bfs to explore all possible direction starting with the rotton ones
        while enque:
            minute+=1
            for _ in range(len(enque)):
                r,c = enque.popleft()
                for dr , dc in directions:
                    nrd = r+dr
                    ncd = c+dc
                    if( min(nrd,ncd)< 0 or nrd >= ROWS or ncd >= COLUMNS or  grid[nrd][ncd] != 1):
                        continue
                    grid[nrd][ncd] = 2
                    enque.append((nrd,ncd))

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 1:
                    return -1
        return minute

        #  how would i know that the entire board is completed and how i am gonna determine the iterations
        # so here we need to return the time if all the oranges in the board is rotton , even if 1 fresh left we need to return 0


        