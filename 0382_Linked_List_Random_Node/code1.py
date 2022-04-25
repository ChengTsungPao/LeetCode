# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = self.getLength(head)
            
    def getLength(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length
    
    def getRandom(self) -> int:
        n = random.randrange(0, self.length)
        node = self.head
        for _ in range(n):
            node = node.next
        return node.val
            

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()