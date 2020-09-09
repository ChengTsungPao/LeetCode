class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if nums.count(0) == nums.count(1):
            return len(nums)
        s = 0
        maxlength = 0
        data = {0:-1}
        for i in range(len(nums)):
            s += nums[i] - (nums[i] == 0)
            if(s not in data):
                data[s] = i
            else:
                maxlength = max(maxlength, i - data[s])
        return maxlength