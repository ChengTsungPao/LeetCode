class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        power = 1
        for i in range(32):
            count = 0
            for num in nums:
                count += (num & power) > 0
            if count >= k: ans += power
            power <<= 1
        return ans