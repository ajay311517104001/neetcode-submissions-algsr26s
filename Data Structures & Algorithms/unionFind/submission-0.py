class UnionFind:
    
    def __init__(self, n: int):
        # Note: AJ
        # This is an heavy understanding oriented algorithm so  make sure you see the drawing or youtube playlist to understand this better


        # basically what is gonna be my data structure to store the nodes
        #  i can use the hashmap and i can use the list (since neetcode used it)
        self.store = [i for i in range(n)]
        # [0,1,1,1,4,5,6,7,8,9]
        #  0 1 2 3 4 5 6 7 8 9
        self.rank = [1]*n

        #  [1,2,0,0,1,1,1,1,1,1]

    def find(self, x: int) -> int:
        # how we can find the root of the component
        # we can find it by traversing to the root node of the component
        # what is my stop point would be
        # when i find the index and the value happens to be the same that is the boss
        #  no optimization at this point
        while x != self.store[x]:
            x = self.store[x]
        return x


        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
        # (1,3) -> will return false, since it is distinct component


    def union(self, x: int, y: int) -> bool:
        # optimization 1 which has rank
        # to make the union we need to find the boss or the root node of the component
        x_root = self.find(x) # 1
        y_root = self.find(y) # 3

        if x_root == y_root:
            return False
        #  don't we need to update when we assign the xroot to yroot or y root to x_root
        # no because we are making a condition if x is greater even if we add y it does not change the height of the tree
        # if y is greater and if we add the x also it does not affect the size of the tree
        if self.rank[x_root] > self.rank[y_root]:
            self.store[y_root] = x_root
            self.rank[y_root] = 0
        elif self.rank[x_root] < self.rank[y_root]:
            self.store[x_root] = y_root
            self.rank[x_root] = 0
        else:
            # when we have the same height lets say we have 2 and 2 when i make the x to y it became 3 my existing tree with 2 nodes is getting added by root node 1 so it the rank of x should turn to 3
            self.store[y_root] = x_root
            self.rank[y_root] = 0
            self.rank[x_root]+=1

        return True

    def getNumComponents(self) -> int:

        return len([i for i in self.rank if i>0])

