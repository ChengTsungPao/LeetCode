class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BST:
    
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        
        def _insert(root, val):
            if not root:
                return Node(val)
            
            if val <= root.val:
                root.left = _insert(root.left, val)
            else:
                root.right = _insert(root.right, val)
                
            return root
        
        self.root = _insert(self.root, val)
        
        
    def search(self, val):
        
        def _search(root, val):
            if not root:
                return float("inf")
            
            if val <= root.val:
                return min(abs(val - root.val), _search(root.left, val))
            else:
                return min(abs(val - root.val), _search(root.right, val))
            
        return _search(self.root, val)
    
    
    def remove(self, val):
        
        def _remove(root, val):
            if not root:
                return None
            
            if val < root.val:
                root.left = _remove(root.left, val)
            elif val > root.val:
                root.right = _remove(root.right, val)
            else:
                if not root.left:
                    node = root.right
                    root.right = None
                    return node
                elif not root.right:
                    node = root.left
                    root.left = None
                    return node
                
                predecessor = root.left
                while predecessor.right:
                    predecessor = predecessor.right
                root.val = predecessor.val
                root.left = _remove(root.left, predecessor.val)
                
            return root
        
        self.root = _remove(self.root, val)
                

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k == 0:
            return False
        
        n = len(nums)
        tree = BST()
        tree.insert(nums[0])
        
        i = 0
        j = 1
        while j < n:
            if tree.search(nums[j]) <= t:
                return True
            
            tree.insert(nums[j])
            j += 1
            
            if j - i > k:
                tree.remove(nums[i])
                i += 1
                
        return False