class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        ans = i = j = 0
        
        while i < len(arr) - 1:
            j = i
            
            # 出現遞減或等於直接continue
            if j < len(arr) - 1 and arr[j] >= arr[j + 1]:
                i = j + 1
                continue
            
            # 出現遞增 j + 1
            while j < len(arr) - 1 and arr[j] < arr[j + 1]:
                j += 1
                
            # 出現邊界或等於直接continue
            if j >= len(arr) - 1 or (j < len(arr) - 1 and arr[j] == arr[j + 1]):
                i = j + 1
                continue
            
            # 出現遞減 j + 1
            while j < len(arr) - 1 and arr[j] > arr[j + 1]:
                j += 1
                
            ans = max(ans, j - i + 1)
            i = j
            
        return ans