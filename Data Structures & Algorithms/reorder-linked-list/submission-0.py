# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid point using the cycle detection algo
        dummy = ListNode()
        dummy_ptr = dummy
        dummy_h = dummy
        last = None
        s=head
        f = head
        while f and f.next:
            s=s.next
            f=f.next.next
        # reverse the second half of the linked list
        # 3 2 1 0
        #         f
        #         t 
        #       l
        first = s.next
        temp = s.next
        s.next =None
        while temp:
            first = first.next
            temp.next = last
            last = temp
            temp = first
        # merge it into the new linked list
        # head and last
        l1 = head
        l2 = last
        while l2:
            dummy_ptr.next = l1
            l1=l1.next
            dummy_ptr = dummy_ptr.next
            dummy_ptr.next = l2
            l2=l2.next
            dummy_ptr = dummy_ptr.next
        dummy_ptr.next = l1
        


        