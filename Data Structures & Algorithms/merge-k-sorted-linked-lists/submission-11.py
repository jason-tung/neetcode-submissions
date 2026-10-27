# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = head = ListNode()
        h = [(lists[i].val, i, lists[i]) for i in range(len(lists)) if lists[i]]
        heapq.heapify(h)
        i = len(lists)
        while h:
            _, _, nxt = heapq.heappop(h)
            head.next = nxt
            head = nxt
            if nxt.next:
                heapq.heappush(h, (nxt.next.val, i, nxt.next))
                i += 1
        return res.next
