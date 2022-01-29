class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i], warehouse[i - 1])
            
        warehouse.reverse()
        boxes.sort()
        
        ans = 0
        i = j = 0
        while i < len(boxes) and j < len(warehouse):
            if boxes[i] <= warehouse[j]:
                ans += 1
                i += 1
            j += 1
            
        return ans