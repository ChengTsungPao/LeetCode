# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        
        def mergeSort(head):
            
            if head == None or head.next == None:
                return head
            
            # 增加一個Head，找preMid
            newHead = ListNode()
            newHead.next = head
            
            slow = newHead
            quick = newHead
            
            while quick and quick.next:
                slow = slow.next
                quick = quick.next.next 
            mid = slow.next
            slow.next = None          
            
            # merge兩個Sorted Linked List
            headPointer = newHead
            node1, node2 = mergeSort(head), mergeSort(mid)

            while node1 and node2:
                if node1.val < node2.val:
                    headPointer.next = node1
                    node1 = node1.next
                else:
                    headPointer.next = node2
                    node2 = node2.next
                headPointer = headPointer.next
                
            while node1:
                headPointer.next = node1
                node1 = node1.next
                headPointer = headPointer.next
                
            while node2:
                headPointer.next = node2
                node2 = node2.next
                headPointer = headPointer.next
                
            headPointer.next = None 
            
            return newHead.next

        return mergeSort(head)
