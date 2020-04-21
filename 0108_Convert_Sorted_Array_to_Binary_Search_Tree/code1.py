# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def inorder(node,left,right):
            index = (left+right)//2
            node.val = nums[index]
            if(index-left>=1):
                node.left = TreeNode(0)
                inorder(node.left,left,index-1)
            if(right-index>=1):
                node.right = TreeNode(0)
                inorder(node.right,index+1,right)            
        if(nums!=[]):
            head = TreeNode(0)
            inorder(head,0,len(nums)-1)        
            return head
        else:
            return None