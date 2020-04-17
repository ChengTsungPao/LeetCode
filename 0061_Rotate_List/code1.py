# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if(head==None or head.next==None): return head
        temp = head
        length = 0
        while(temp!=None):
            length += 1
            temp = temp.next
        rot = (length-k)%length
        if(rot==0): return head
        temp = head
        tmp = 0
        print(length)
        while(tmp<length-1):
            tmp += 1
            if(tmp==rot):
                newhead = temp
                temp = temp.next
                newhead.next = None
                newhead = temp
            else:
                temp = temp.next
        temp.next = head    
        return newhead