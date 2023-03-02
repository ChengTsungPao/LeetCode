class Node:
    def __init__(self, leftIndex, rightIndex, val = 0, _min = -float("inf"), minIndex = -1):
        self.left = None
        self.right = None
        self.val = val
        self.min = (_min, minIndex)
        self.range = (leftIndex, rightIndex)

class SegmentTree:
    def __init__(self, nums):
        self.root = self.build(nums, 0, len(nums) - 1)
        
    def build(self, nums, leftIndex, rightIndex):
        if leftIndex == rightIndex:
            val = _min = nums[leftIndex]
            minIndex = leftIndex
            return Node(leftIndex, rightIndex, val, _min, minIndex)
        
        midIndex = leftIndex + (rightIndex - leftIndex) // 2
        root = Node(leftIndex, rightIndex)
        root.left = self.build(nums, leftIndex, midIndex)
        root.right = self.build(nums, midIndex + 1, rightIndex)
        root.min = max(root.left.min, root.right.min)
        return root
    
    def queryMinIndex(self, leftIndex, rightIndex):
        
        def _query(root, leftIndex, rightIndex):
            
            if root.range[0] == root.range[1]:
                return root.min

            midIndex = root.range[0] + (root.range[1] - root.range[0]) // 2
            if midIndex >= rightIndex:
                return _query(root.left, leftIndex, rightIndex)
            elif midIndex + 1 <= leftIndex:
                return _query(root.right, leftIndex, rightIndex)
            else:
                return min(_query(root.left, leftIndex, midIndex), _query(root.right, midIndex + 1, rightIndex))
            
        return _query(self.root, leftIndex, rightIndex)[1]

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        n = len(target)
        self.ST = SegmentTree(target)
        
        def recur(i, j, current_sub):
            if i == j:
                return target[i] - current_sub
            elif i > j:
                return 0
            
            k = self.ST.queryMinIndex(i, j)
            require_sub = target[k] - current_sub
            return require_sub + recur(i, k - 1, current_sub + require_sub) + recur(k + 1, j, current_sub + require_sub)
        
        return recur(0, n - 1, 0)