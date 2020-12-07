class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums):
            if nums == []:
                return [[]]
            ans = []
            for i in range(len(nums)):
                for visited in dfs(nums[:i] + nums[i + 1:]):
                    ans += [[nums[i]] + visited]
            return ans
        return dfs(nums)