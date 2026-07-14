# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ret = []
        q = deque([root])
        while q:
            p = q.popleft()
            if p == None:
                ret.append('_')
            else:
                ret.append(str(p.val))
                q.append(p.left)
                q.append(p.right)
        return ','.join(ret)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        node = TreeNode(data[0]) if data[0] != '_' else None
        q = deque([node])
        i = 1
        while q:
            p = q.popleft()
            if p:
                p.left = TreeNode(data[i]) if data[i] != '_' else None
                q.append(p.left)
                i += 1
                p.right = TreeNode(data[i]) if data[i] != '_' else None
                q.append(p.right)
                i += 1
        return node


