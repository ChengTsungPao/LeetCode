class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums = collections.Counter(nums)

        def dfs(nums, choose):
            if(choose == length):
                return [[]]
            ans = []
            for key in nums.keys():
                if(nums[key] != 0):
                    nums[key] -= 1
                    for visited in dfs(nums, choose + 1):
                        ans += [[key] + visited]                    
                    nums[key] += 1
            return ans

        return dfs(nums, 0)