# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        
        def getNextPosition(i, j, index):
            di, dj = direction[index]
            i_, j_ = i + di, j + dj
            if not (0 <= i_ < m and 0 <= j_ < n) or grid[i_][j_] >= 0:
                return getNextPosition(i, j, (index + 1) % 4)
            return i_, j_, index
        
        grid = [[-1] * n for _ in range(m)]
        i = j = index = 0
        while head:
            grid[i][j] = head.val
            if head.next: 
                i, j, index = getNextPosition(i, j, index)
            head = head.next
            
        return grid