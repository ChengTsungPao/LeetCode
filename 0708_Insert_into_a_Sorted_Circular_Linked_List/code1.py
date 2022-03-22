"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)
        
        if not head:
            node.next = node
            return node
        elif id(head) == id(head.next):
            node.next = head
            head.next = node
            return head            
        
        pointer = head
        while True:
            # 介於兩val之間 或 頭尾
            if pointer.val <= insertVal <= pointer.next.val or \
               insertVal >= pointer.val > pointer.next.val  or \
               pointer.val > pointer.next.val >= insertVal:
                node.next = pointer.next
                pointer.next = node
                break
            
            pointer = pointer.next
            
            # 若繞一圈沒有插入點，隨意插入
            if id(pointer) == id(head):
                node.next = pointer.next
                pointer.next = node
                break
            
        return head        