# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1, current = list1.next, list1
            else:
                current.next = list2
                list2, current = list2.next, list2
        if list1 or list2:
            current.next = list1 if list1 else list2

        return dummy.next
'''
1. current and dummy are initialized as instances of the ListNode class.
    dummy is used to keep track of the head of the merged list,
    while current is used to traverse and append nodes to the merged list.
2. A while loop runs until both list1 and list2 are not empty.
    Inside the loop, it compares the values of the nodes at the head of list1 and list2.
    The smaller value is appended to the merged list using the current pointer.
    The corresponding list1 or list2, and current are then moved to the next nodes.
3. If either list1 or list2 still has elements left after the loop completes,
    the remaining elements are appended to the merged list.
4. Finally, the head of the merged list (excluding the dummy node) is returned.
'''