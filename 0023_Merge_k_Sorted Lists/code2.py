# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        lists = list(filter(lambda x: x != None, lists))
        
        def merge(head1, head2):
            
            head = ListNode()
            
            if head1.val < head2.val:
                head.val = head1.val
                head1 = head1.next
            else:
                head.val = head2.val
                head2 = head2.next
            
            temp = head
            
            while head1 and head2:
                temp.next = ListNode()
                
                if head1.val < head2.val:
                    temp.next.val = head1.val
                    head1 = head1.next
                else:
                    temp.next.val = head2.val
                    head2 = head2.next
                
                temp = temp.next
                    
            if head1:
                temp.next = head1
            elif head2:
                temp.next = head2
            else:
                temp.next = None

            return head
        
        while len(lists) > 1:
            
            head1 = lists.pop()
            head2 = lists.pop()
            
            lists.insert(0, merge(head1, head2))

        if lists == []:
            return None
        else:
            return lists[0]