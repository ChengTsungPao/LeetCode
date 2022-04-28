class Node:
    def __init__(self, index = 0, val = 0):
        self.index = index
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, index, val):
        def _insert(root, index, val):
            if not root:
                return Node(index, val)
            if val < root.val:
                root.left = _insert(root.left, index, val)
            elif val == root.val:
                root.index = index
            else:
                root.right = _insert(root.right, index, val)
            return root
        self.root = _insert(self.root, index, val)

    def searchMaxClose(self, val):
        def _searchMaxClose(root, val):
            if not root:
                return float("inf"), float("inf")
            if val <= root.val:
                return min((root.val - val, root.index), _searchMaxClose(root.left, val))
            else:
                return _searchMaxClose(root.right, val)
        return _searchMaxClose(self.root, val)[1]

    def searchMinClose(self, val):
        def _searchMinClose(root, val):
            if not root:
                return float("inf"), float("inf")
            if val < root.val:
                return _searchMinClose(root.left, val)
            else:
                return min((val - root.val, root.index), _searchMinClose(root.right, val))
        return _searchMinClose(self.root, val)[1]        

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:        

        n = len(arr)
        
        tree = BST()
        tree.insert(n - 1, arr[n - 1])
        
        dpOdd = [False] * n
        dpOdd[n - 1] = True
        dpEven = [False] * n
        dpEven[n - 1] = True

        for index in range(n - 2, -1, -1):
            evenIndex = tree.searchMaxClose(arr[index])
            oddIndex = tree.searchMinClose(arr[index])
            
            if evenIndex != float("inf") and dpEven[evenIndex] == True:
                dpOdd[index] = True
            if oddIndex != float("inf") and dpOdd[oddIndex] == True:
                dpEven[index] = True
                
            tree.insert(index, arr[index])
        
        return sum(dpOdd)