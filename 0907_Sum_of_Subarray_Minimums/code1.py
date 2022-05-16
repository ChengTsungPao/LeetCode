class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        n = len(arr)
        MOD = 10 ** 9 + 7
        
        def findMin(i, j):
            index, _min = -1, float("inf")
            for k in range(i, j + 1):
                if arr[k] < _min:
                    index, _min = k, arr[k]
            return index
        
        def divide_and_conquer(i, j):
            if i == j:
                return arr[i]
            elif i > j:
                return 0
            
            k = findMin(i, j)
            ans = arr[k] * (k - i + 1) * (j - k + 1)
            ans += divide_and_conquer(i, k - 1)
            ans += divide_and_conquer(k + 1, j)
            ans %= MOD
            
            return ans
        
        return divide_and_conquer(0, n - 1)