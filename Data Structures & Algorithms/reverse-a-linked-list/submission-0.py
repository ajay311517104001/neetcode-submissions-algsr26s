# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # assign 
        #  last to NOne
        #  middle to head
        # first to head
        # N<-0<-1<-2<-3
                    #      t
                    #   l
                   
                    #      f   
        last = None
        first = head
        temp = head
        while temp:
            first = first.next
            temp.next = last
            last = temp
            temp = first
        return last        