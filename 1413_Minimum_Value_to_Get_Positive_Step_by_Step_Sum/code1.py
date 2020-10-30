class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        if(nums == []):
            return 1
        ans = [0]
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            ans.append(s)
        return abs(min(ans) - 1)