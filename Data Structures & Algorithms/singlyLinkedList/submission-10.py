class Node:
    def __init__(self , data , next_val = None):
        self.data = data
        self.next = next_val



class LinkedList:
    
    def __init__(self):
        # dummy node
        self.head = Node(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        # traverse till the index node
        #  -1 -> 0->1-> null
        #        0  1
        curr = self.head.next
        i=0
        while curr and i < index:
            i+=1
            curr = curr.next
        if curr:
            return curr.data
        return -1
        # if node , return data
        # return -1

    def insertHead(self, val: int) -> None:
        #  -1 -> 0- >null
        #   h    t
        curr = self.head
        new_node = Node(val)
        if self.head.next:
            new_node.next = curr.next
            curr.next = new_node
        else:
            curr.next = new_node
            self.tail = new_node


        # -1 - > 0 -> 1-> 2-> null
        

    def insertTail(self, val: int) -> None:
        #  -1 - > null
        #   ht
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node
        #  -1 -> 0 -> 1 -> null
            # h       t

    def remove(self, index: int) -> bool:
        #  remove in the middle, remove 1
        # -1 - > 0 -> 1-> 2-> null
        #        0    1   2t

        # remove in the start , remove 0
        #  -1 -> 0 -> 1 -> null
        #        0    1t 

        #  remove at the end
        #  -1 -> 0 -> 1 -> null , remove 1
        #   h     t0    1  

        #  we need travese before the index curr
        curr = self.head
        i=0
        while curr and i< index:
            i+=1
            curr = curr.next
        #  if next of curr is tail, re assign the tail to the curr
        # if curr.next == self.tail:
        #     self.tail = curr
        #     self.tail.next = None
        #     return True
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
                self.tail.next = None
            if curr.next and curr.next.next:
                curr.next = curr.next.next
            return True
        return False


        #  remove hte element , return true
        # return False



        

    def getValues(self) -> List[int]:
        curr = self.head.next
        l = []
        while curr:
            l.append(curr.data)
            curr = curr.next
        return l
        
