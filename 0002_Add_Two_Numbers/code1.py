# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        index = 0
        while(l1!=None):
            num1 = num1 + l1.val*10**(index)
            l1 = l1.next
            index += 1
        num2 = 0
        index = 0
        while(l2!=None):
            num2 = num2 + l2.val*10**(index)
            l2 = l2.next
            index += 1
        num = str(num1 + num2)
        head = ListNode(0)
        temp = head
        for i in range(len(num)-1,-1,-1):
            temp.val = int(num[i])
            if(i!=0):
                temp.next = ListNode(0)
                temp = temp.next
            else:
                temp.next = None
        return head