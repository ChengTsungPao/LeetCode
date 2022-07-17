class Node:
    def __init__(self, leftIndex, rightIndex, val = 0, _max = 0):
        self.left = None
        self.right = None
        self.val = val
        self.max = _max
        self.range = (leftIndex, rightIndex)

class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.root = self.build(0, len(self.nums) - 1)
        
    def build(self, leftIndex, rightIndex):
        if leftIndex == rightIndex:
            return Node(leftIndex, rightIndex, self.nums[leftIndex], self.nums[leftIndex])
        
        midIndex = leftIndex + (rightIndex - leftIndex) // 2
        root = Node(leftIndex, rightIndex)
        root.left = self.build(leftIndex, midIndex)
        root.right = self.build(midIndex + 1, rightIndex)
        root.val = root.left.val + root.right.val
        root.max = max(root.left.max, root.right.max)
        return root
    
    def getValue(self, index):
        if index >= len(self.nums):
            return -1
        
        return self.nums[index]
    
    def update(self, index, delta):
        
        def _update(root, index, delta):
            if not (root and root.range[0] <= index <= root.range[1]):
                return

            root.val -= delta
            _update(root.left , index, delta)
            _update(root.right, index, delta)
            
            if not root.left and not root.right:
                root.max = root.val
            else:
                leftMax = root.left.max if root.left else 0
                rightMax = root.right.max if root.right else 0
                root.max = max(leftMax, rightMax)
        
        _update(self.root, index, delta)
        self.nums[index] -= delta
    
    def querySum(self, leftIndex, rightIndex):
        
        def _query(root, leftIndex, rightIndex):
        
            if leftIndex == root.range[0] and rightIndex == root.range[1]:
                return root.val

            midIndex = (root.range[0] + root.range[1]) // 2
            if midIndex >= rightIndex:
                return _query(root.left, leftIndex, rightIndex)
            elif midIndex + 1 <= leftIndex:
                return _query(root.right, leftIndex, rightIndex)
            else:
                return _query(root.left, leftIndex, midIndex) + _query(root.right, midIndex + 1, rightIndex)
            
        return _query(self.root, leftIndex, rightIndex)
    
    def queryFirstValidRow(self, leftIndex, rightIndex, k):
        
        def _query(root, leftIndex, rightIndex):
            
            if root.max < k:
                return float("inf")
            if root.range[0] == root.range[1]:
                return root.range[0]

            midIndex = (root.range[0] + root.range[1]) // 2
            if midIndex >= rightIndex:
                return _query(root.left, leftIndex, rightIndex)
            elif midIndex + 1 <= leftIndex:
                return _query(root.right, leftIndex, rightIndex)
            else:
                ret = _query(root.left, leftIndex, midIndex)
                return _query(root.right, midIndex + 1, rightIndex) if ret == float("inf") else ret
            
        return _query(self.root, leftIndex, rightIndex)

class BookMyShow:

    def __init__(self, n: int, m: int):
        self.ST = SegmentTree([m] * n)
        self.scatterRow = 0
        self.n = n
        self.m = m

    def gather(self, k: int, maxRow: int) -> List[int]:  
        gatherRow = self.ST.queryFirstValidRow(self.scatterRow, maxRow, k)     
        if gatherRow == float("inf"):
            return []
        
        gatherCol = self.m - self.ST.getValue(gatherRow)
        self.ST.update(gatherRow, k)
        self.scatterRow += self.ST.getValue(self.scatterRow) == 0
        return [gatherRow, gatherCol]
        
    def scatter(self, k: int, maxRow: int) -> bool:
        if self.scatterRow > maxRow or self.ST.querySum(self.scatterRow, maxRow) < k:
            return False
        
        while k > 0:
            emptySeat = self.ST.getValue(self.scatterRow)
            if k >= emptySeat:
                self.ST.update(self.scatterRow, emptySeat)
                self.scatterRow += 1
            else:
                self.ST.update(self.scatterRow, k)
            k -= emptySeat
        return True
    
# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)