class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        from sortedcontainers import SortedList
        
        n = len(arr)
        MOD = 10 ** 9 + 7
        
        ans = 0
        arr = sorted([(arr[i], i) for i in range(n)])
        
        bst = SortedList()
        bst.add(-1)
        bst.add(n)
        
        for num, index in arr:
            right = bst.bisect_left(index)
            left = right - 1
            
            lower = bst[left] + 1
            upper = bst[right] - 1
            
            ans += num * (index + 1 - lower) * (upper + 1 - index)
            ans %= MOD
            
            bst.add(index)
            
        return ans