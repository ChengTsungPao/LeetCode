class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        # head increasing range
        i = 0
        while i < n - 1 and arr[i] <= arr[i + 1]:
            i += 1
        
        # tail decreasing range
        j = n - 1
        while j > 0 and arr[j - 1] <= arr[j]:
            j -= 1
            
        if i == n - 1:
            return 0

        # find cut index
        ans = min(n - i - 1, j)
        for k in range(i + 1):
            cut = bisect.bisect_left(arr, arr[k], j, n)
            ans = min(ans, cut - k - 1)
            
        return ans