# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def lrpair(root):
            if not root:
                return (-1,-1, 0)
            left, right = lrpair(root.left), lrpair(root.right)
            ld,rd = max(left[:2]) + 1, max(right[:2]) + 1
            most = max(ld + rd, left[2], right[2])
            return (ld, rd, most)
        return lrpair(root)[2]


#         3
#     1       null
# null   2