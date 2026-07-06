# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node,biggest=-101):
            if not node:
                return 0
            ret = 0
            if node.val >= biggest:
                biggest = node.val
                ret = 1
            return ret + helper(node.left, biggest) + helper(node.right, biggest)
        return helper(root)