# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        #  find the length of the linked list
        t= head
        total=1
        while t and t.next:
            t = t.next
            total+=1
        # find the index need to be deleted
        index = total - n
        # index = 2
        temp.next = head
        for _ in range(index):
            temp = temp.next
        
        temp.next = temp.next.next
        
        return dummy.next