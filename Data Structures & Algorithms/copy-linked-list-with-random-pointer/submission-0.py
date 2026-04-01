"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import collections
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # we can create the new linked list by iterating the one need to be copied
        # then we need to make the random assignment using hash map
        dummy = Node(-1)
        d_head = dummy
        d_temp = dummy
        temp = head
        t = head
        h_map = {}
        # iterate the original linked list
        # #       1->2->3->4-> None
        #                       t
        # # dummy->1->2->3->4->None
        #                   d
        while temp:
        #  make a new node and add it to dummy
        # take the original node instance
            dummy.next = Node(temp.val)
        #  iterate the original
            h_map[temp] = dummy.next
            temp = temp.next
            
        #  iterate the dummy
            dummy = dummy.next
            
            
        
        d_temp = d_temp.next
        while d_temp:
            if t.random is not None:
                d_temp.random = h_map[t.random]
            d_temp = d_temp.next
            t=t.next
        return d_head.next
        
