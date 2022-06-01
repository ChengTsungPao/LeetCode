class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        
        n = len(warehouse)
        
        prefixMin = [float("inf")] * n
        suffixMin = [float("inf")] * n
        
        prefixMin[ 0] = warehouse[ 0]
        suffixMin[-1] = warehouse[-1]
        
        minIndex = 0
        
        for i in range(1, n):
            prefixMin[ i] = min(prefixMin[ i - 1], warehouse[ i])
            suffixMin[~i] = min(suffixMin[~i + 1], warehouse[~i])
            
            if prefixMin[i - 1] > warehouse[i]:
                minIndex = i
        
        ans = 0
        i = minIndex
        j = i + 1
        for box in sorted(boxes):
            
            while i >= 0 and box > prefixMin[i]:
                i -= 1
            while j < n and box > suffixMin[j]:
                j += 1
            
            _min, isLeft = float("inf"), None
            if i >= 0:
                _min, isLeft = min((_min, isLeft), (prefixMin[i], True))
            if j < n:
                _min, isLeft = min((_min, isLeft), (suffixMin[j], False))
                
            if isLeft == None:
                break
            
            ans += 1
            if isLeft:
                i -= 1
            else:
                j += 1
                
        return ans