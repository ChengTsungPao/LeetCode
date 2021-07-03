class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        
        status = []
        for i in range(len(arr)):
            if arr[i]:
                status.append(i)

        if status == []:
            return [0, len(arr) - 1]
        elif len(status) % 3 != 0:
            return [-1 ,-1]
        
        area = len(status) // 3
        for i in range(area - 1):
            left  = status[i + 0 * area + 1] - status[i + 0 * area]
            mid   = status[i + 1 * area + 1] - status[i + 1 * area]
            right = status[i + 2 * area + 1] - status[i + 2 * area]
            if left != mid or mid != right:
                return [-1, -1]
                
        leftIndex  = status[1 * area - 1] + (len(arr) - status[-1] - 1)
        rightIndex = status[2 * area - 1] + (len(arr) - status[-1] - 1) + 1
        if leftIndex < status[1 * area] and rightIndex <= status[2 * area]:
            return [leftIndex, rightIndex]
        
        return [-1 ,-1]