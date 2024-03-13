# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum_map = {}
        current = dummy
        prefix_sum = 0
        while current:
            # print(current.val)
            # print(prefix_sum, prefix_sum_map)
            # print()
            prefix_sum += current.val
            prefix_sum_map[prefix_sum] = current
            current = current.next
        
        current = dummy
        prefix_sum = 0
        # print("*****")
        while current:
            # print(current.val)
            # print(prefix_sum, prefix_sum_map)
            # print()
            prefix_sum += current.val
            if prefix_sum in prefix_sum_map:
                current.next = prefix_sum_map[prefix_sum].next
            current = current.next

        return dummy.next