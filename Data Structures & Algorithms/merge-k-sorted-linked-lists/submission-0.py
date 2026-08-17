# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for list in lists:
            curr = list
            while curr is not None:
                if curr.val is not None:
                    heap.append(curr.val)
                    curr = curr.next

        heapq.heapify(heap)
       
        head = ListNode(heapq.heappop(heap), None) if heap else None
        
        curr = head
        while heap:
            curr.next = ListNode(heapq.heappop(heap), None)
            curr = curr.next

        return head
        