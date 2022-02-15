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

    def update(self, index, delta):

        def updateTree(node, index, val):
            if node == None:
                return None
            if index <= (node.sumRange[0] + node.sumRange[1]) // 2:
                updateTree(node.left, index, val)
            else:
                updateTree(node.right, index, val)
            node.val += val - self.nums[index]

        updateTree(self.node, index, self.nums[index] + delta)
        self.nums[index] += delta

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


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        # time complexity: O(nlogn)
        # space complexity: O(n)   
        # n = maxNum - minNum + 1

        # 概念: 將SegmentTree的delta都設為1，來統計數量
        # 方法: 由右而左update，在quary的時候只會有該index右邊的數字參與，且只有較小的數字會被加起來 (非rank直接用數值大小)
        # 注意: 但須注意不能quary與自己大小相同的數字 (nums[i] - 1)
        
        # 比起另一個方法少了一個sort，速度會較快，但較耗空間，且無法處理有小數點的情況
        
        _max = -float("inf")
        _min = float("inf")
        for num in nums:
            _max = max(_max, num)
            _min = min(_min, num)
        
        ST = SegmentTree([0] * (_max - _min + 1))
        
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i] - _min
            ans.append(ST.quary(0, num - 1))
            ST.update(num, 1)
            
        return ans[::-1]