
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head= Node(-1)
        self.tail = self.head
       

    def get(self, index: int) -> int:
        #  iterate till the index
        temp = self.head.next
        i = 0    #1
        while i < index and temp:
        #  check if temp and return data
            i+=1
            temp = temp.next
        if temp:
            return temp.data
        return -1 # out of bount

       

        

    def insertHead(self, val: int) -> None:
        #  -1 -> 1
        #  -1 
        #  create a node
        temp = Node(val)
        temp.next = self.head.next
        self.head.next = temp
        if not temp.next:
            self.tail = temp



    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        
    def remove(self, index: int) -> bool:
        #  iterate till before the index
        #  make the links , return true
        #  return false
        i =0
        temp = self.head
        while i < index and temp:
            i+=1
            temp = temp.next 
        # make lilnks
        if temp and temp.next:
            if temp.next == self.tail:
                self.tail = temp
            temp.next = temp.next.next
            return True

        return False


    def getValues(self) -> List[int]:
        l = []
        temp = self.head.next
        while temp != None:
            l.append(temp.data)
            temp = temp.next
        return l

        
