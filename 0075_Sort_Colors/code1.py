class Solution:
    def sortColors(self, nums: List[int]) -> None:
        data = collections.Counter(nums)
        s = 0
        for i in sorted(data.keys()):
            nums[s : s + data[i]] = [i]*data[i]
            s += data[i]