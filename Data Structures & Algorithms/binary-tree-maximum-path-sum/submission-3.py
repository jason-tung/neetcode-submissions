# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m = -math.inf
        def sol(node):
            if not node:
                return 0
            # take l, r, both, none
            l,r = sol(node.left), sol(node.right)
            best_sum_here = node.val + max(l, r, l + r, 0)
            nonlocal m
            m = max(m, best_sum_here)
            return node.val+max(l, r, 0)
        sol(root)
        return m