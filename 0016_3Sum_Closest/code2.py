class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        nums.sort()
        
        ans = float("inf")
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                sum_ = nums[i] + nums[j]
                k = bisect.bisect_left(nums, target - sum_, j + 1, n)
                
                if k < n and abs(target - (sum_ + nums[k])) < abs(target - ans):
                    ans = sum_ + nums[k]
                if k > j + 1 and abs(target - (sum_ + nums[k - 1])) < abs(target - ans):
                    ans = sum_ + nums[k - 1]
                    
        return ans