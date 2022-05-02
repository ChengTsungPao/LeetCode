class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        nums.sort()
        
        ans = float("inf")
        for i in range(n - 2):
            
            j = i + 1
            k = n - 1
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                
                if sum_ > target:
                    ans = min(ans - target, sum_ - target, key = abs) + target
                    k -= 1
                elif sum_ < target:
                    ans = min(ans - target, sum_ - target, key = abs) + target
                    j += 1
                else:
                    ans = target
                    break
                    
            if ans == target:
                break
                    
        return ans