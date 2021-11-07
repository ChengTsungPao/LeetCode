# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def recur(node):
            nonlocal ans
            
            if node == None:
                return {}
            
            left = recur(node.left)
            right = recur(node.right)
            
            merge = left.copy()
            for key in right.keys():
                merge[key] = merge.get(key, 0) + right[key]
            
            # 單個node總和
            if node.val == targetSum:
                ans += 1
                
            # node加上node的child的總和
            if targetSum - node.val in merge:
                ans += merge[targetSum - node.val]
            
            count_sum = {}
            for key in merge.keys():
                count_sum[key + node.val] = merge[key]
            count_sum[node.val] = count_sum.get(node.val, 0) + 1
            
            return count_sum
        
        ans = 0        
        recur(root)
        
        return ans