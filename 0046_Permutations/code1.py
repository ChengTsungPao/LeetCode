class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(nums, _list):
            if(nums==[]):
                ans.append(_list)
                return None
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], _list + [nums[i]])
        dfs(nums, [])
        return ans