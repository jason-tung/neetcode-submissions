# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def sol(a,b):
            if not (a and b):
                return not (bool(a) ^ bool(b))
            return a.val == b.val and sol(a.left, b.left) and sol(a.right, b.right)
        return sol(p,q)