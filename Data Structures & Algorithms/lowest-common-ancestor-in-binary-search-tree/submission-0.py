# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lowest = None
        def helper(root, p, q):
            if not root:
                return (False, False)
            cur = (root.val==p.val, root.val==q.val)
            left, right = helper(root.left, p, q), helper(root.right, p, q)
            res = tuple(a or b or c for a,b,c in zip(cur, left, right))
            nonlocal lowest
            if all(res) and not lowest:
                lowest = root
            return res
        helper(root, p, q)
        return lowest
        