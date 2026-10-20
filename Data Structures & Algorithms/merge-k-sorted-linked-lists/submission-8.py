# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = head = ListNode()
        i = 0
        h = []
        for l in lists:
            if l:
                h.append((l.val, i, l))
                i += 1
        heapq.heapify(h)
        while h:
            val, _, l = heapq.heappop(h)
            head.next = l
            if l.next:
                heapq.heappush(h, (l.next.val, i, l.next))
                i += 1
            head = head.next
        return res.next