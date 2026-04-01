class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # I need to ther region if the 'O' in the border which is connected with the regrion

        # Intution:
        # Inorder to mark the region surrounded by 'X', first i need for find if the 'O' present in the border
        # If that presents in the border whether it is connected with the region which is present inside the board
        # we need to ignore the region if a part of the region is present on the boarder.
        # mark the 'O' to "X" if the 'O' are not present in the border
        # ignore the region if the part of the region present inside on the border and rest mark all 'O' as 'X'

        # iterate the four borders and collect the 'O' which are present inside the border
        # for each and every 'O' which forms a region mark them as visited

        # mark all the cells which has 'O' and which is not in the visited to 'X' then return 

        

        if not board:
            return board
        visited = set()
        enque= collections.deque()
        ROWS, COLUMNS = len(board), len(board[0])
        # get the top and bottom row to the visited

        for c in range(COLUMNS):
            if board[0][c] == 'O':
                visited.add((0,c))
                enque.append((0,c))
            if board[ROWS-1][c] == 'O':
                visited.add((ROWS-1,c))
                enque.append((ROWS-1, c))
        # get the left and right column to the visted
        for r in range(ROWS):
            if board[r][0] == 'O':
                visited.add((r,0))
                enque.append((r,0))
            if board[r][COLUMNS-1] == 'O':
                visited.add((r,COLUMNS-1))
                enque.append((r,COLUMNS-1))

        directions = [[0,-1],[0,1],[1,0],[-1,0]]
        def dfs(enque, visited):
            while enque:
                r,c = enque.popleft()
                for dr, dc in directions:
                    nrd,ncd = r + dr, c+dc
                    if(min(nrd,ncd)<0 or (nrd,ncd) in visited or nrd>= ROWS or ncd>= COLUMNS or board[nrd][ncd] == 'X'):
                        continue
                    enque.append((nrd,ncd))
                    visited.add((nrd,ncd))
        dfs(enque,visited)


        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c]= 'X'
        return
                        


        