class Solution:
    # Attempting to solve this problem with optimal soultuion or approach
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # we need to have 2 different sets to keep track of the visited calls for Pacifc and Atlantic
        if not heights:
            return heights

        p_visited = set()
        a_visited = set()

        p_enque = collections.deque()
        a_enque = collections.deque()

        ROWS , COLUMNS = len(heights), len(heights[0])
        # add the initial index to the appropriate sets
        # Pacific
        for c in range(COLUMNS):
            p_visited.add((0,c))
            p_enque.append((0,c))
        for r in range(ROWS):
            p_visited.add((r,0))
            p_enque.append((r,0))

        # Atlantic
        for c in range(COLUMNS):
            a_visited.add((ROWS-1,c))
            a_enque.append((ROWS-1,c))
        for r in range(ROWS):
            a_visited.add((r,COLUMNS-1))
            a_enque.append((r,COLUMNS-1))


        # from there perfrom the bfs from both the oceans individually and perform the intersection
        directions = [ [0,-1], [0,1], [1,0], [-1,0]]
        def bfs(enque, visited):
            while enque:
                r,c = enque.popleft()
                for dr , dc in directions:
                    nrd, ncd = r+dr , c+dc
                    if (min(nrd, ncd)<0 or nrd >= ROWS or ncd>=COLUMNS or (nrd,ncd) in visited or heights[r][c]> heights[nrd][ncd]):
                        continue
                    enque.append((nrd,ncd))
                    visited.add((nrd,ncd))
        bfs(p_enque, p_visited)
        bfs(a_enque, a_visited)

        return list(p_visited.intersection(a_visited))


        