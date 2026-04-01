# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse both of the linked list
        #  n<-1   2 -> 3 -> null
        #          f
        #   l   t
        # last = None
        # temp =l1
        # first = l1
        # while temp:
        #     first = first.next
        #     temp.next = last
        #     last=temp
        #     temp = first
            
        # h1 = last

        # last = None
        # temp =l2
        # first = l2
        # while temp:
        #     first = first.next
        #     temp.next = last
        #     last=temp
        #     temp = first
            
        # h2 = last
        # take the head of both linked list
        # iterate the linked list and get the value of list1 and list2


        # Note : No need to reverse coz the one we got is already reversed just do the calculation and perform the linked list

        dummy = ListNode()
        k = dummy
        h1 = l1
        h2 = l2
        carry = 0
        while h1 or h2: #can extrend the condition for carry like or carry which make sure our carry is added to the linked list atlast
            val1 = h1.val if h1 else 0
            val2 = h2.val if h2 else 0
            # sum the value take the last digit and update the carry if any
            total = val1+val2 + carry
            carry = total//10
            s = total%10
            # take the last digit and create a node and linked it to the new linked list
            dummy.next = ListNode(s)
            # update the new new linked list position
            dummy = dummy.next
            # update the linked list one position and two position
            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None
            
        if carry:
            dummy.next = ListNode(carry)

        # last = None
        # temp =h.next
        # first = h.next
        # while temp:
        #     first = first.next
        #     temp.next = last
        #     last=temp
        #     temp = first
            
        return k.next
        # in the end check if the if carry if it is not zero udpate it in the linked list
        #  if it is zero ignore
        # return the linked list
        