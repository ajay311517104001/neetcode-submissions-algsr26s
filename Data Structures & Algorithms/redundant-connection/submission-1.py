class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(0,len(edges)+1)]
        rank = [1]*(len(edges)+1)

    
        def find(x):
            # if x == parent[x]:
            #     return x
            # #  this makes the other nodes parent as the root of the current component
            # parent[x] = find(parent[x])
            # return x

            while x!= parent[x]:
                x = parent[x]
            return x
        
        def union(x,y):
            x_root = find(x)
            y_root = find(y)

            if x_root == y_root:
                # detects the cycle here
                return False
            
            if rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            elif rank[y_root] > rank[x_root]:
                parent[x_root] = y_root
            else:
                parent[y_root] = x_root
                rank[x_root]+=1
            return True


        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge 

            


        