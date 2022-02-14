class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        
        dp = [1] * len(nums)
        track = {}        
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i] % nums[j] == 0 or nums[i] % nums[j] == 0) and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    track[i] = j

        index = 0
        for i in range(1, len(dp)):
            if dp[i] > dp[index]:
                index = i

        ans = [nums[index]]
        while index in track:
            index = track[index]
            ans.append(nums[index])
                    
        return ans