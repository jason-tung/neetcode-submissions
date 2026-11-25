# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def sol(p,q):
            if not p or not q:
                return not p and not q
            return p.val == q.val and sol(p.left, q.left) and sol(p.right, q.right)
        return sol(p,q)