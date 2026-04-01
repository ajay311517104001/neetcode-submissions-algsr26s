class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS = len(heights)
        COLS = len(heights[0])
        p_visited = set()
        a_visited = set()

        p_enque = deque()
        a_enque = deque()

        direction = [[0,-1], [0,1] , [1,0] ,[-1,0]]


        for c in range(COLS):
            p_visited.add((0, c))
            p_enque.append((0, c))
            a_visited.add((ROWS - 1, c))
            a_enque.append((ROWS - 1, c))

        for r in range(ROWS):
            p_visited.add( (r , 0))
            p_enque.append(( r,0))
            a_visited.add((r , COLS-1))
            a_enque.append((r,COLS-1))


       

        def bfs(enque , visited):

            while enque:
                r ,c = enque.popleft()
                for dr,dc in direction:
                    ndr = r +dr
                    ndc = c+dc
                    if min(ndr ,ndc) < 0 or ndr >=ROWS or ndc >= COLS or (ndr,ndc) in visited or heights[r][c] > heights[ndr][ndc]:
                        continue
                    visited.add((ndr , ndc))
                    enque.append((ndr,ndc))

        bfs(p_enque , p_visited)
        bfs(a_enque , a_visited)

        return  list(p_visited.intersection(a_visited))



            



        
        