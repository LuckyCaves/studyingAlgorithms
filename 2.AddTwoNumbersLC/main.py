# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        numbers = 0
        carry = 0
        l3 = ListNode()
        copy = l3


        while (l1 != l2 and carry == 0):
            if l1 is not None:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0

            if l2 is not None:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0

            numbers = (val1 + val2) + carry
            carry = numbers % 10


            l3.next = ListNode(carry)
            l3 = l3.next
            carry = numbers // 10

        return copy.next
