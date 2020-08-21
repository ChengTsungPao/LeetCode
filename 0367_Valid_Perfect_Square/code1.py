class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left < right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid
        return num == 1