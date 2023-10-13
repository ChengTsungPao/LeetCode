class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        
        M = pow(10, 9) + 7
        n = len(nums)
        
        count = [0] * 32
        for i, num in enumerate(nums):
            for j in range(32):
                count[j] += (num & 1)
                num >>= 1

        ans = 0
        for _ in range(k):
            num = 0
            for j in range(31, -1, -1):
                num <<= 1
                if count[j] > 0:
                    num += 1
                    count[j] -= 1
            ans += (num * num)
            
        return ans % M