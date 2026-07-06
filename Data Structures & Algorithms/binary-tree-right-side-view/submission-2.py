# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = [101] * 100
        def helper(node, level=0):
            if not node:
                return
            nonlocal levels
            levels[level] = node.val
            helper(node.left, level+1)
            helper(node.right, level+1)
        helper(root)
        return [k for k in levels if k != 101]
        