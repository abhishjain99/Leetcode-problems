# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = dummy = ListNode(0, head)
        for i in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        deleted = slow.next
        slow.next = deleted.next if deleted else None
        del deleted
        return dummy.next