class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        n = len(arr)
        sorted_arr = sorted(arr)
        
        ans = 0
        bitmap1 = bitmap2 = 2 ** n - 1
        for i in range(n):
            bitmap1 -= (1 << arr[i])
            bitmap2 -= (1 << sorted_arr[i])
            
            if bitmap1 == bitmap2:
                ans += 1
        
        return ans