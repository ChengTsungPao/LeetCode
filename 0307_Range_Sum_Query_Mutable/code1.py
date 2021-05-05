class Binary_Indexed_Tree:
    
    def __init__(self, size):
        self.size = size + 1
        self.data = [0 for _ in range(self.size)]
        
    def lowbit(self, index):
        return index & (-index)
        
    def update(self, index, delta):
        while index < self.size:
            self.data[index] += delta
            index += self.lowbit(index)
            
    def query(self, index):
        s = 0
        while index > 0:
            s += self.data[index]
            index -= self.lowbit(index)
        return s

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.BIT = Binary_Indexed_Tree(len(self.nums))
        for i in range(len(self.nums)):
            self.BIT.update(i + 1, self.nums[i])

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.BIT.update(index + 1, delta)
        self.nums[index] = val
        
    def sumRange(self, left: int, right: int) -> int:    
        return self.BIT.query(right + 1) - self.BIT.query(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)