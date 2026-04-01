# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # brute force TC -> O(N) and space O(1)
        dummy = ListNode()
        temp = dummy
        # #  find the length of the linked list
        # t= head
        # total=1
        # while t and t.next:
        #     t = t.next
        #     total+=1
        # # find the index need to be deleted
        # index = total - n
        # # index = 2
        # temp.next = head
        # for _ in range(index):
        #     temp = temp.next
        
        # temp.next = temp.next.next
        
        # return dummy.next

        #  Instead of going thru the entire linked list and again iterating half or full of the linked list
        #  we can implement it using two pointer technique

        #  initialize right pointer to head
        r = head
        # iterate till n times
        #  1-> 2 -> 3 -> 4 -> None
                    # r
        for _ in range(n):
            r = r.next
        # again initialize the left pointer at the dummy node
        # make the left pointer pointing the head node
        temp.next = head
        l = temp
        # iterate both the pointers till the s reaches none
        while r!=None:
            r = r.next
            l=l.next
        # then place the l next to the l next next
        l.next = l.next.next
        # return
        return temp.next
        
