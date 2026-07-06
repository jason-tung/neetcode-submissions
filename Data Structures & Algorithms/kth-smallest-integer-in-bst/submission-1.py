# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1
        def helper(root, cnt):
            if not root:
                return 0
            l = helper(root.left, cnt)
            current_index = cnt + l + 1
            if current_index == k:
                nonlocal ans
                ans = root.val
            r = helper(root.right, current_index)
            return l + r + 1
        helper(root, 0)
        return ans
            
                
                