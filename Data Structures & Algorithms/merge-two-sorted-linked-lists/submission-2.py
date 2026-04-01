# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # # assign the head to the start of list 1
        # # # when both the head are same
                        
        # # # list1   1  2    4  d
        # #           | /\  / \   t1
        # # # list2   1   3     5
        # #                    t
        # # #  take t2 as head 

        # t1 = list1
        # t2 = list2
        
        # if t1 and not t2:
        #     return t1
        # if t2 and not t1:
        #     return t2
        # if not t1 and not t2:
        #     return None

        # if t1.val == t2.val:
        #     head = t1
        #     tail = t1
        #     t1 = t1.next
        # elif t1.val < t2.val:
        #     tail = t1
        #     head = t1
        #     t1 = t1.next
            
        # else:
        #     head = t2
        #     tail = t2
        #     t2 = t2.next

        # #  chaining
        # #  need to set the limit
        # while  t1 and t2:
        #     if t1.val<t2.val:
        #         d = t1.next
        #         tail.next = t1
        #         tail = t1
        #         t1 = d

        #     else:
        #         d = t2.next
        #         tail.next = t2
        #         tail = t2
        #         t2 =d
        # if t1:
        #     tail.next = t1
        #     tail = t1
        # else:
        #     tail.next = t2
        #     tail = t2
        # return head


        # Gold standard or an easier version
        # create a dummy node
        # set a tail pointer to it
        dummy = ListNode()
        tail = dummy

        #  iterate
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next

