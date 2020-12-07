class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums = collections.Counter(nums)
        
        def dfs(nums, choose, dp = {}):
            key = str(nums) 
            if key not in dp:
                if(choose == length):
                    return [[]]
                dp[key] = []
                for node in nums.keys():
                    if(nums[node] != 0):
                        nums[node] -= 1
                        for visited in dfs(nums, choose + 1, dp):
                            dp[key] += [[node] + visited]                    
                        nums[node] += 1
            return dp[key]
        
        return dfs(nums, 0)