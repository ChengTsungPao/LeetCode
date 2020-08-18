class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = 1
        ans = []
        for i in range(len(nums)):
            ans.append(s)
            s *= nums[i]
        s = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= s
            s *= nums[i]
        return ans