# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def solve(node):
            if not node:
                return node
            lookahead=node
            for _ in range(k - 1):
                lookahead = lookahead.next
                if not lookahead:
                    return node
            prev=solve(lookahead.next)
            for _ in range(k):
                nxt=node.next
                node.next=prev
                prev=node
                node=nxt
            return prev
            
        return solve(head)
        # start on 0 (always start 1 before next group of k)
        # look ahead k
        # if not k avail, return
        # mark this node
        # reverse last k nodes
        # loop
        # 0 A B C D E 
        # 0 B A D C E