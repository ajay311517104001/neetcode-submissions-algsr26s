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
        # dummy = Node(-1)
        # d_head = dummy
        # d_temp = dummy
        # temp = head
        # t = head
        # h_map = {}
        # # iterate the original linked list
        # # #       1->2->3->4-> None
        # #                       t
        # # # dummy->1->2->3->4->None
        # #                   d
        # while temp:
        # #  make a new node and add it to dummy
        # # take the original node instance
        #     dummy.next = Node(temp.val)
        # #  iterate the original
        #     h_map[temp] = dummy.next
        #     temp = temp.next
            
        # #  iterate the dummy
        #     dummy = dummy.next

        # d_temp = d_temp.next
        # while d_temp:
        #     if t.random is not None:
        #         d_temp.random = h_map[t.random]
        #     d_temp = d_temp.next
        #     t=t.next
        # return d_head.next


        # Implementation of Two pass approach

        # TC -O(N) where N is the number of nodes in the linked list
        # SC - O(N), Where N is the number of elements in the dict
        #  we have a dict to store the nodes
        # node_dict = {None : None}

        # # create key nodes and add it in the node
        # temp = head
        # while temp:
        #     copy = Node(temp.val)
        #     node_dict[temp] = copy
        #     temp = temp.next
        # # map the next value and random value to the copied nodes using the dict
        # curr = head
        # while curr:
        #     node_dict[curr].next = node_dict[curr.next]
        #     node_dict[curr].random = node_dict[curr.random]
        #     curr = curr.next

        # h = head
        # return node_dict[h]
        # return the value


        # Implementation in one pass approach
        # If the values doesn't exist in the dictionary, it will create a copy of the original node set a default value
        # In upcoming iterations it will check if the node exists in dict if yes it will set the value and then set next and random

        # create a node dict
        node_dict = collections.defaultdict(lambda: Node(0))
        # add none to it to handle the edge cases
        node_dict[None] = None

        temp = head
        # iterate the original list
        while temp:
        # set the value if node exists else it will automatically creates the node
            node_dict[temp].val = temp.val
        # set the next pointer
            node_dict[temp].next = node_dict[temp.next] # In first iteration itself it will check , if node doesn't exist it will create the default Node
        # set the value pointer
            node_dict[temp].random = node_dict[temp.random]
        # increment the link
            temp = temp.next

        #  return the head via the dict
        h= head
        return node_dict[h]
