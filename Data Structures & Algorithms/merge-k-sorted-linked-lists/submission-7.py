# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1,l2):
            res = dummy = ListNode()
            while l1 or l2:
                if not l2 or l1 and l1.val <= l2.val:
                    n = l1
                    l1 = l1.next
                elif not l1 or l2 and l2.val <= l1.val:
                    n = l2
                    l2 = l2.next
                res.next = n
                res = res.next
                n.next = None
            return dummy.next
        def helper(lists,i, j):
            if i <= j:
                if i == j:
                    return lists[i]
                m = (i + j) // 2
                l = helper(lists, i, m)
                r = helper(lists, m + 1, j)
                return merge(l, r)
        return helper(lists, 0, len(lists) - 1)
        
            
                