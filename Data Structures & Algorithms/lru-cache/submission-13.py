class Node:
    def __init__(self, key = None, val = None):
        self.next = None
        self.key = key
        self.val = val
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # create a double linked list 
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        # create a map to locate the node in the doubly linked list
        self.cap = capacity
        # create a flag to save the capacity
        self.cache = {}
        self.limit=0

        # [h]<->[(val)]<->[t]
        

    def get(self, key: int) -> int:
        # check the cache if it has key
        #  if not :
        # return -1
        if key in self.cache:
            temp = self.cache[key]
            # node deletion
            d = temp
            d.prev.next = d.next
            d.next.prev = d.prev
            # node insertion in front
            h = self.head
            temp.next = h.next
            temp.prev = h
            h.next = temp
            temp.next.prev = temp
            # update dict
            self.cache[key] = temp
            return temp.val

        else:
            return -1
        #  if yes:
        # Recently used 
        #  get the node delete it 
        # add the same node after head
        # return the value

        

    def put(self, key: int, value: int) -> None:
        # check if the capacity is full and and key exists
        # pop the key 
        if key in self.cache:    
        # update the key
            node = self.cache[key]
            if node.key == key:
                node.val = value
                temp = node
                # delete node
                node.prev.next = node.next
                node.next.prev = node.prev
                # insert it in the front
                h = self.head
                temp.next = h.next
                temp.prev = h

                h.next = temp
                temp.next.prev = temp
                self.cache[key] = temp

        elif len(self.cache) == self.cap:
            temp = self.tail.prev
            self.tail.prev = temp.prev
            temp.prev.next = self.tail   

            del self.cache[temp.key]

            h = self.head
            temp = Node(key,value)
            temp.next = h.next
            temp.prev = h
            h.next = temp
            temp.next.prev = temp
            
            # add it to dict
            self.cache[key] = temp
        else:
            h = self.head
            temp = Node(key,value)
            temp.next = h.next
            temp.prev = h
            h.next = temp
            temp.next.prev = temp
            
            # add it to dict
            self.cache[key] = temp
        
        # add it to front

        # return

    