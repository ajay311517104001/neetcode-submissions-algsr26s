class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # what u would do now?
        # create the enque
        if not grid:
            return 0
        enque= collections.deque()
        ROWS,COLUMNS = len(grid) , len(grid[0])
        # add the first value since it would be empty
        enque.append((0,0))
        # declare all the directions in the array
        count = 0
        visited=set()
        visited.add((0,0))
        direction = [ [0,-1],[0,1],[1,0],[-1,0]]
        # till the enque is empty loop it
        while enque:
            # iterate the direction
            for _ in range(len(enque)):
                # pop the left element for the enque
                r,c = enque.popleft()
                if (r == ROWS-1 and c == COLUMNS-1):
                    return count
                for dr,dc in direction:
                    nrd = r+dr
                    ncd = c+dc
                # check the condition if it is over bounds or under bounds and not one and should not be visited
                    if (min(nrd,ncd)<0 or nrd >= ROWS or ncd >= COLUMNS or (nrd,ncd) in visited or grid[nrd][ncd]== 1):
                        continue
                # continue
                    visited.add((nrd,ncd))
                # add them to the visited
                    enque.append((nrd,ncd))
            count+=1
        return -1
        # add them to the queue
        # increment the length
        # return the length
        