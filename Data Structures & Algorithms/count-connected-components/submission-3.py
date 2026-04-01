class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        self.nodes = [ i for i in range(0,n)]
        self.rank = [1] * n
        self.count = 0

        def find(no):
            if self.nodes[no] == no:
                return no
            self.nodes[no]= find(self.nodes[no])
            return self.nodes[no]
            
        def union(n1,n2):
            n1_master = find(n1)
            n2_master = find(n2)
            if n1_master!= n2_master:
                if self.rank[n1_master] >= self.rank[n2_master]:
                    self.nodes[n2_master] = n1_master
                    self.rank[n2_master]+=1
                elif self.rank[n2_master] > self.rank[n1_master]:
                    self.nodes[n1_master] = n2_master
                    self.rank[n1_master]+=1
                # else:
                #     self.nodes[n2_master] = n1_master
                #     self.rank[n2_master]+=1
                self.count+=1
                
        

        for con in edges:
            union(con[0],con[1])
        
        return n - self.count