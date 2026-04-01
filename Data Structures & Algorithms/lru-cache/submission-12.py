class LRUCache:

    def __init__(self, capacity: int):
        # save the capacity
        self.cap = capacity
        # cache = [(2,20),(3,30)]
        self.cache = []
        

    def get(self, key: int) -> int:
        # if the key exists in the cache which O(n) time 
        for index , item in enumerate(self.cache):
            if item[0] == key:
                 # delete the tuple from the list and add to the last
                val = self.cache.pop(index)
                self.cache.append(val)
                return item[1]

        return -1
        #  return the key
        # if not found
        #  return -1
        

    def put(self, key: int, value: int) -> None:
        # if the limit is full 
        
        # delete the key 
        for index , item in enumerate(self.cache):
            if item[0] == key:
                # delete the tuple from the list and add to the last
                val = self.cache.pop(index)
                self.cache.append((key,value))
                return
            
        if len(self.cache) == self.cap:
            self.cache.pop(0)
            self.cache.append((key,value))
        elif len(self.cache) < self.cap:
            self.cache.append((key,value))
        # # add it to the last
        
        # #  if the limit is < than the key exists
        # # i can add them to the last
        #     for index , item in enumerate(self.cache):
        #             if item[0] == key:
        #                 # delete the tuple from the list and add to the last
        #                 val = self.cache.pop(index)
        #                 self.cache.append((key,value))
        #                 return
            
        
        
