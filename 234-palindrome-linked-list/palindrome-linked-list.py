# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        fast = head
        ans = True
        # print('head', head.val, fast.val)
        while fast.next is not None:
            stack.append(head.val)
            head = head.next
            fast = fast.next.next
            if fast is None:
                break
            if fast.next is None:
                head = head.next
        
        while head and stack:
            elem = stack.pop()
            if elem == head.val:
                ans = True
            else:
                ans = False
                break
            head = head.next

        return ans