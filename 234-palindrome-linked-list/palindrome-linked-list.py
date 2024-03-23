# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # # Using slow, fast, and stack
        # stack = []
        # fast = head
        # ans = True
        # while fast and fast.next:
        #     stack.append(head.val)
        #     head = head.next
        #     fast = fast.next.next
        #     if fast is None:
        #         break
        #     if fast.next is None:
        #         head = head.next

        # while head and stack:
        #     elem = stack.pop()
        #     if elem == head.val:
        #         ans = True
        #     else:
        #         ans = False
        #         break
        #     head = head.next

        # return ans




        # # Using slow, fast, and reverse
        slow = head
        fast = head
        dummy = None
        ans = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is None: break
            if fast.next is None: slow = slow.next
        curr = slow
        while slow:
            curr = slow.next
            slow.next = dummy
            dummy = slow
            slow = curr

        while head and dummy:
            if head.val != dummy.val:
                ans = False
                break
            else: ans = True
            head = head.next
            dummy = dummy.next

        return ans