# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        

        def merge(list1 , list2):
            dummy = ListNode(-1)
            h = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    dummy.next = ListNode(list1.val)
                    dummy = dummy.next
                    list1 = list1.next
                else:
                    dummy.next = ListNode(list2.val)
                    dummy = dummy.next
                    list2 = list2.next
            dummy.next = list1 if list1 else list2
            return h.next 

        
        for l in range(1,len(lists)):
            lists[l] = merge(lists[l], lists[l-1])
        return lists[-1] if lists else None









