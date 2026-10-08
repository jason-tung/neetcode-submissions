"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, l1: 'Optional[Node]') -> 'Optional[Node]':
        # d<l1.address -> l2.address>
        if not l1:
            return None
        d = defaultdict(lambda: Node(0))
        head = l1
        while l1:
            l2 = d[l1]
            l2.val, l2.next, l2.random = l1.val, d[l1.next] if l1.next else None, d[l1.random] if l1.random else None
            l1 = l1.next
        return d[head]