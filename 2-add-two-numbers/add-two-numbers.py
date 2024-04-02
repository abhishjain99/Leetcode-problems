# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode(0)
        # tail = dummy
        # carry = 0
        # while l1 is not None or l2 is not None or carry != 0:
        #     d1 = l1.val if l1 is not None else 0
        #     d2 = l2.val if l2 is not None else 0
        #     s = d1 + d2 + carry
        #     carry = s // 10
        #     s = s % 10

        #     sum_node = ListNode(s)
        #     tail.next = sum_node
        #     tail = tail.next

        #     l1 = l1.next if l1 is not None else None
        #     l2 = l2.next if l2 is not None else None
        
        # ans = dummy.next
        # dummy.next = None
        # return ans

        dummy = ListNode()
        ans = dummy
        total = carry = 0
        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            carry = total // 10
            total %= 10
            dummy.next = ListNode(total)
            dummy = dummy.next
        return ans.next