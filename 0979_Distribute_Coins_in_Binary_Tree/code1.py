# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        # 概念: 對於每個node而言，需流入或流出 abs(total_coins - nodes)
        # 特性: 利用到tree的性質，只要拿掉一個node，整張圖會一分為二
        
        ans = 0
        def recur(root):
            nonlocal ans
            
            if not root:
                return 0, 0
            
            coinsL, nodesL = recur(root.left)
            coinsR, nodesR = recur(root.right)
            
            coins = coinsL + coinsR + root.val
            nodes = nodesL + nodesR + 1
            ans += abs(coins - nodes)
            
            return coins, nodes
        
        recur(root)
        return ans