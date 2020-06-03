class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = collections.Counter(nums)
        return min(tmp,key=tmp.get)