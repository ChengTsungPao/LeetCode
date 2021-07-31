class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(x, y):
            return int(y + x) - int(x + y)
        
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        nums.sort(key = functools.cmp_to_key(compare))
        
        return "".join(nums) if nums[0] != "0" else "0"
