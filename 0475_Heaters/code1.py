class Node:
    def __init__(self, value = -1):
        self.left = None
        self.right = None
        self.val = value

class BST:
    def __init__(self, heaters):
        self.root = self.build(sorted(heaters))
        
    def build(self, heaters):
        
        def _build(left, right):
            if left == right:
                return Node(heaters[left])
            elif left > right:
                return None
            
            mid = left + (right - left) // 2
            root = Node(heaters[mid])
            root.left = _build(left, mid - 1)
            root.right = _build(mid + 1, right)
            
            return root
        
        return _build(0, len(heaters) - 1)
    
    def search(self, val):
        
        def _search(root, val):
            if not root:
                return float("inf")
            
            if val < root.val:
                return min(abs(val - root.val), _search(root.left, val))
            elif val > root.val:
                return min(abs(val - root.val), _search(root.right, val))
            else:
                return 0
            
        return _search(self.root, val)
    
    
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        tree = BST(heaters)
        
        ans = 0
        for pos in houses:
            ans = max(ans, tree.search(pos))

        return ans