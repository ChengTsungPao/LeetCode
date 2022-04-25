# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
    
    def getRandom(self) -> int:
        value = 0
        count = 1
        node = self.head
        while node:
            if random.random() < 1 / count:
                value = node.val
            node = node.next
            count += 1
        return value
            

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()