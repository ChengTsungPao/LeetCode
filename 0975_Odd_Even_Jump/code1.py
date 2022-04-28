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

        graph = collections.defaultdict(list) 
        for index in range(n - 2, -1, -1):
            evenIndex = tree.searchMaxClose(arr[index])
            oddIndex = tree.searchMinClose(arr[index])

            graph[evenIndex, False].append(index)
            graph[oddIndex, True].append(index)
            
            tree.insert(index, arr[index])

        def recur(index, isOdd):
            ret = set([index]) if isOdd else set()
            if len(graph[index, isOdd]) == 0:
                return ret
            for nextIndex in graph[index, isOdd]:
                ret |= recur(nextIndex, not isOdd)
            return ret

        return len(recur(n - 1, True) | recur(n - 1, False))