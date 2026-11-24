"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        def get(node):
            if not node:
                return None
            if node not in d:
                d[node] = Node(node.val)
            return d[node]
        res = head
        while head:
            other = get(head)
            other.next = get(head.next)
            other.random = get(head.random)
            head = head.next
        return get(res)