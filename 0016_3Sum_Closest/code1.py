class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float("inf")
        for i in range(len(nums)-2):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                temp = nums[i] + nums[start] + nums[end]
                if(temp == target):
                    ans = target
                    break
                elif(temp > target):
                    ans = min(ans - target, temp - target, key = abs) + target
                    end -= 1
                else:
                    ans = min(ans - target, temp - target, key = abs) + target
                    start += 1
        return ans