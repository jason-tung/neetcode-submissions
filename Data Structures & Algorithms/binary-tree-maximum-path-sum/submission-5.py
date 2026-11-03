# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = -math.inf
        def sol(node):
            nonlocal best
            if not node:
                return 0
            l,r = max(0, sol(node.left)), max(0, sol(node.right))
            best = max(best, node.val + l + r)
            return node.val+max(l, r)
        sol(root)
        return best