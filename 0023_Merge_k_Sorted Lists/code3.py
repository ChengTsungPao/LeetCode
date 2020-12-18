# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        if lists == [] or set(lists) == {None}:
            return None
        
        pointer = ans = ListNode()
        
        heap = []
        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
                
        while heap:
            val, index = heapq.heappop(heap)
            if lists[index] != None:
                heapq.heappush(heap, (lists[index].val, index))
                lists[index] = lists[index].next
            
            pointer.val = val
            
            if heap:
                pointer.next = ListNode()
                pointer = pointer.next
            else:
                pointer.next = None
        
        return ans