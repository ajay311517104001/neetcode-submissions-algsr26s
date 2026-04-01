class trieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = ''

class Trie:
    def __init__(self):
        self.root = trieNode()


    def create(self, board , words):
            #create word tree with trie
            # iterate the 2d board and check if the nodes are matching if matches return 
            # result list
            
            
    
            for w in words:
                curr = self.root
                for c in w:
                    if c not in curr.children:
                        curr.children[c] = trieNode()
                    curr = curr.children[c]
                curr.isWord = True
                curr.word = w
            return self.root
        
    def check(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return 'not found'
                
            curr = curr.children[c]
        return curr.word

    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #create word tree with trie
        # iterate the 2d board and check if the nodes are matching if matches return 
        # result list
     
        t = Trie()
        t.create(board , words)
        directions = [(0,1) , (0,-1) , (-1,0) , (1,0) ]

        visited = set()

        result = set()
        def dfs(r,c , curr):
            if r>= ROW or c >= COLUMN or min(r,c) < 0 or (r,c) in visited or board[r][c] not in curr.children:
                return
            
            visited.add((r,c))
            curr = curr.children[board[r][c]]
            if curr.isWord:
                result.add(curr.word)
            
            
            
            

            for dr, dc in directions:
                ndr = r+dr
                ndc = c + dc
                dfs(ndr , ndc , curr)
            visited.remove((r,c))
            return



        ROW = len(board)
        COLUMN = len(board[0])

        curr = t.root
        for r in range(0,ROW):
            for c in range(0,COLUMN):
                    dfs(r,c, curr)
        return list(result)
                            
                            
                                


                        









                                

        