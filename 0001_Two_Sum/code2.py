class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        status = collections.defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in status:
                return [status[target - nums[i]], i]
            else:
                status[nums[i]] = i