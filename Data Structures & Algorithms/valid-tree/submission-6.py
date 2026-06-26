class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        class unf:
            def __init__(self):
                self.parent = [i for i in range(n)]
                self.rank = [0] * n

            def find(self , x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self,x,y):
                px = self.find(x)
                py = self.find(y)
                if px == py:
                    return True
                
                if self.rank[px] > self.rank[py]:
                    self.parent[py] = px
                elif self.rank[py] > self.rank[px]:
                    self.parent[px] = py
                else:
                    self.parent[py] = px
                    self.rank[px]+=1
                return False
        
        if len(edges) != n - 1:
            return False
            
        uf = unf()
        for e1, e2 in edges:
            if uf.union(e1,e2):
                return False
        return True


