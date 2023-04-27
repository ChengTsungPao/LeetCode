class Solution:
    def bulbSwitch(self, n: int) -> int:
        # 看有幾個完全平方數 (概念: 完全平方數有奇數個因數，非完全平方數反之)
        
        left, right = 0, n
        
        findIndex = 0
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 <= n:
                findIndex = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return findIndex