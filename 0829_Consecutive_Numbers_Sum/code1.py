class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        ans = 0
        for num in range(1, int((N * 2) ** 0.5) + 1):
            if (N * 2) % num == 0 and (num % 2 == 1 or (N * 2 // num) % 2 == 1):
                ans += 1
        return ans