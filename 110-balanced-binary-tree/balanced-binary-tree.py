# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, node):
        if node is None: return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        if abs(left_depth-right_depth) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False