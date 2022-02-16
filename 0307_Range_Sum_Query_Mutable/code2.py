class Node:
    def __init__(self, leftIndex, rightIndex, val = 0):
        self.left = None
        self.right = None
        self.sumRange = (leftIndex, rightIndex)
        self.val = val
            
class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.node = self.build(0, len(self.nums) - 1)
    
    def build(self, leftIndex, rightIndex):
        if leftIndex == rightIndex:
            return Node(leftIndex, rightIndex, self.nums[leftIndex])
        node = Node(leftIndex, rightIndex)
        index = (node.sumRange[0] + node.sumRange[1]) // 2
        node.left = self.build(leftIndex, index)
        node.right = self.build(index + 1, rightIndex)
        node.val = node.left.val + node.right.val
        return node

    def update(self, index, val):

        def updateTree(node, index, val):
            if node == None:
                return None
            if index <= (node.sumRange[0] + node.sumRange[1]) // 2:
                updateTree(node.left, index, val)
            else:
                updateTree(node.right, index, val)
            node.val += val - self.nums[index]

        updateTree(self.node, index, val)
        self.nums[index] = val

    def quary(self, leftIndex, rightIndex):
        
        def _quary(node, leftIndex, rightIndex):
            if not node:
                return 0
            elif leftIndex == node.sumRange[0] and rightIndex == node.sumRange[1]:
                return node.val
            index = (node.sumRange[0] + node.sumRange[1]) // 2
            if rightIndex <= index:
                return _quary(node.left, leftIndex, rightIndex)
            elif leftIndex > index:
                return _quary(node.right, leftIndex, rightIndex)
            else:
                return _quary(node.left, leftIndex, index) + _quary(node.right, index + 1, rightIndex)  
            
        return _quary(self.node, leftIndex, rightIndex)
        
        
class NumArray:
    def __init__(self, nums: List[int]):
        self.ST = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.ST.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.ST.quary(left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)