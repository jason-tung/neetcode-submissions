# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = dummy = ListNode()
        counter = count()
        heap = [(l.val if l else 0, next(counter), l) for l in lists]
        heapq.heapify(heap)
        while heap:
            (val, _, pop) = heapq.heappop(heap)
            if pop:
                res.next = pop
                res = res.next
                pop = pop.next
                heapq.heappush(heap, (pop.val if pop else 0, next(counter), pop))
        res.next = None
        return dummy.next
        
        