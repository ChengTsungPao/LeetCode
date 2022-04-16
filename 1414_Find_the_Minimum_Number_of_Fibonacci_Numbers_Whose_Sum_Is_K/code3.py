class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        def fibonacci(n):
            return int((((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n) / 5 ** 0.5)
        
        def binarySearch(left, right, target):
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                fn = fibonacci(mid)
                if fn <= target:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        n = 2
        while fibonacci(n) < k:
            n *= n
        
        ans = 0
        while k > 0:
            n = binarySearch(0, n, k)
            k -= fibonacci(n)
            ans += 1
            
        return ans