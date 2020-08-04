class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        first = {}
        for i in range(len(nums)):
            if nums[i] in first and i - first[nums[i]] <= k:
                return True
            first[nums[i]] = i
        return False