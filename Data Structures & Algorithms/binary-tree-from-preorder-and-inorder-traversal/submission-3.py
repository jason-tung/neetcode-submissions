# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inindex = {n:i for (i,n) in enumerate(inorder)}
        def build_partition(i, l, r):
            if l >= r:
                return None
            val = preorder[i]
            m = inindex[val]
            node = TreeNode(val)
            node.left = build_partition(i + 1, l, m)
            node.right = build_partition(i + 1 + m - l, m + 1, r)
            return node
        return build_partition(0, 0, len(inorder))
                
                