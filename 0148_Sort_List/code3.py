# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        dummyHead = ListNode(0, head)
        self.quickSort(dummyHead, None)
        return head       
        
    def quickSort(self, dummyHead, dummyTail):
        if id(dummyHead.next) == id(dummyTail):
            return

        left, right = self.partition(dummyHead, dummyTail)
        self.quickSort(dummyHead, left)
        self.quickSort(right, dummyTail)
        
    def partition(self, dummyHead, dummyTail):
        tail = self.getTailNode(dummyHead, dummyTail)
        pivotNode = self.getRandomNode(dummyHead, dummyTail)
        pivot = pivotNode.val
        pivotNode.val, tail.val = tail.val, pivotNode.val

        left = dummyHead.next
        cur = dummyHead.next
        while cur != tail:
            if cur.val < pivot:
                left.val, cur.val = cur.val, left.val
                left = left.next
            cur = cur.next
                
        right = left
        cur = left
        while cur != tail:
            if cur.val == pivot:
                right.val, cur.val = cur.val, right.val
                right = right.next
            cur = cur.next
        right.val, tail.val = tail.val, right.val
        return left, right
    
    def getRandomNode(self, dummyHead, dummyTail):
        node = dummyHead.next
        count = 1
        randomNode = None
        while node != dummyTail:
            if random.random() < 1 / count:
                randomNode = node
            count += 1
            node = node.next
        return randomNode
    
    def getTailNode(self, dummyHead, dummyTail):
        node = dummyHead.next
        tailNode = None
        while node != dummyTail:
            tailNode = node
            node = node.next
        return tailNode        
