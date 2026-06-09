# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # we can do like l1 + l2 hen + l3 and then +l4 etc.. 
        # we can group them like (l1,l2) (l3,l4) (l5,l6) etc..

        if not lists:
            return None

        def mergelist(l1,l2):
            dummy = ListNode()
            curr = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next 
            
            curr.next = l1 if l1 else l2
            return dummy.next



        while len(lists) != 1:
            mergedlists = []

            for i in range(0 , len(lists) , 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedlists.append(mergelist(l1,l2))
            lists = mergedlists

        
        return lists[0]

