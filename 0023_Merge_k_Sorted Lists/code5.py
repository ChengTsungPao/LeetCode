# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(head1, head2):
            
            dummy = ListNode()
            pointer = dummy
            
            while head1 and head2:
                if head1.val <= head2.val:
                    pointer.next = head1
                    head1 = head1.next
                else:
                    pointer.next = head2
                    head2 = head2.next
                pointer = pointer.next
                    
            if head1:
                pointer.next = head1
                    
            if head2:
                pointer.next = head2
            
            return dummy.next
        
        while len(lists) > 1:
            newLists = []
            while lists:
                head1 = lists.pop() if lists else None
                head2 = lists.pop() if lists else None
                newLists.append(merge(head1, head2))
            lists = newLists
            
        return lists[0] if lists else None