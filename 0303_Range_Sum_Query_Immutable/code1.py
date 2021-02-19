class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0] + nums
        for i in range(1, len(self.nums)):
            self.nums[i] += self.nums[i - 1]
        
    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j + 1] - self.nums[i]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)