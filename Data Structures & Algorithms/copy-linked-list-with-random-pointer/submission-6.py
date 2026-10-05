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
        if not head:
            return None
        def get(head):
            if head not in d:
                d[head] = Node(head.val)
            return d[head]
        dummy = head
        while head:
            new_head = get(head)
            if head.next:
                new_head.next = get(head.next)
            if head.random:
                new_head.random = get(head.random)
            head = head.next
        return get(dummy)
        