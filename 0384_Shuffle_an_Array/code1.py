class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums.copy()
        self.currentNums = nums.copy()

    def reset(self) -> List[int]:
        self.currentNums = self.nums.copy()
        return self.currentNums
        
    def shuffle(self) -> List[int]:
        for i in range(len(self.currentNums)):
            index = random.randrange(0, len(self.currentNums))
            self.currentNums[i], self.currentNums[index] = self.currentNums[index], self.currentNums[i]
        return self.currentNums
        
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()