class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums = collections.Counter(nums)
        ans = []
        def dfs(nums, _list):
            if(len(_list) == length):
                ans.append(_list)
                return None
            for key in nums.keys():
                if(nums[key] != 0):
                    nums[key] -= 1
                    dfs(nums, _list + [key])
                    nums[key] += 1
        dfs(nums, [])
        return ans
