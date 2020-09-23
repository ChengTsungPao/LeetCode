class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        status = collections.Counter(nums)
        return min(status, key = status.get)