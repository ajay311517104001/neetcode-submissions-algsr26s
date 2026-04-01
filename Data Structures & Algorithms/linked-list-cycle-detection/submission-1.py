# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # initialize the slow pointer
        slow = head
        #  initialize the fast pointer
        fast = head
        # iterate fast
        while fast and fast.next:
        # move slow pointer to one step
            slow = slow.next
        #  move fast pointer to 2 steps
            fast= fast.next.next
        #  check if the slow and fast pointer met
            if slow == fast:
                return True
        #  if yes, return true
        # return false
        return False

        # edge case
        #  if only one node exists?
        #  what if there is a cycle
        # what if there i no cycle


        