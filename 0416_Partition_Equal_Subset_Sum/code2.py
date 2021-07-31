class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2:
            return False
        
        nums.sort()
        
        dp = [True]
        dpSet = [set()]
        for weight in range(1, total // 2 + 1):
            dp.append(False)
            dpSet.append(set())
            for i in range(len(nums)):
                if weight - nums[i] < 0:
                    break
                elif dp[weight - nums[i]] and i not in dpSet[weight - nums[i]]:
                    dp[-1] = True
                    dpSet[-1] |= set([i]) | dpSet[weight - nums[i]]
                    break

        return dp[-1]
