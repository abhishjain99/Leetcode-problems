# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = head
        carry = ListNode()
        while curr is not None:
            curr = curr.next
            c_val = curr.val if curr != None else 0
            summ = dummy.val * 2 + (c_val * 2) // 10
            dummy.val = summ % 10
            if summ > 9 and dummy == head:
                    carry.val = summ // 10
                    carry.next = head
                    head = carry
            dummy = dummy.next
        return head