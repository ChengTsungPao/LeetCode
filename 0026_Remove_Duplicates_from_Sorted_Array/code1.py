class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(collections.Counter(nums).keys())[:]
        return len(nums)
