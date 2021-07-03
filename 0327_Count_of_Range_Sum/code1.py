class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        
        choose = [0]
        nums.insert(0, 0)
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            choose.append(nums[i])
        choose.sort()

        ans = 0
        for i in range(len(nums)):
            del choose[bisect.bisect_left(choose, nums[i])]
            ans += bisect.bisect_right(choose, nums[i] + upper) - bisect.bisect_left(choose, nums[i] + lower)

        return ans