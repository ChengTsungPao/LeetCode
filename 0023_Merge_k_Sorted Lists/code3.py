# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        headPointer = {i: head for i, head in enumerate(lists) if head}
        heap = [(head.val, i) for i, head in enumerate(lists) if head]
        heapq.heapify(heap)
        
        dummy = ListNode()
        pointer = dummy
        
        while heap:
            _, i = heapq.heappop(heap)
            node = headPointer[i]
            nextNode = node.next
            headPointer[i] = nextNode
            
            pointer.next = node
            pointer = pointer.next
            pointer.next = None
            
            if nextNode:
                heapq.heappush(heap, (nextNode.val, i))
                
        return dummy.next