class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        n = len(nums)
        _sum = sum(nums)
        
        def condition(value):
            index = 0
            for _ in range(m):
                s = 0
                while index < n and s + nums[index] <= value:
                    s += nums[index]
                    index += 1
            return index == n
        
        left = _sum // m
        right = _sum + 1
        while left < right:
            mid = left + (right - left) // 2
            if not condition(mid):
                left = mid + 1
            else:
                right = mid

        return left