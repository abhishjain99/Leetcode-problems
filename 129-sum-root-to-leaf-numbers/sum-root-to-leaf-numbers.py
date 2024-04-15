# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def DFS(node, current):
            if node:
                if not node.left and not node.right:
                    return current * 10 + node.val
                ans = 0
                ans += DFS(node.left, current * 10 + node.val)
                ans += DFS(node.right, current * 10 + node.val)
                return ans
            else:
                return 0

        return DFS(root, 0)