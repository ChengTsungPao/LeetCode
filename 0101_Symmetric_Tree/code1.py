# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        self.data = []
        def preorder1(self,node):
            if(node==None):
                return
            else:
                self.data.append(node.val)
            self.data.append("0")
            preorder1(self,node.left)
            self.data.append("1")
            preorder1(self,node.right)
            self.data.append("2")
        self.count = 0
        def preorder2(self,node):
            if(node==None):
                return
            elif(self.count>=len(self.data)):
                return 0
            elif(node.val!=self.data[self.count]):
                return 0
            else:
                self.data[self.count] = node.val
                self.count += 1
            if(self.data[self.count]!="0"): return 0
            self.count += 1
            if(preorder2(self,node.right)==0): return 0
            if(self.data[self.count]!="1"): return 0
            self.count += 1
            if(preorder2(self,node.left)==0): return 0
            if(self.data[self.count]!="2"): return 0
            self.count += 1
        if(root==None):
            return 1
        if(root.left==None and root.right==None):
            return 1
        elif(root.left==None and root.right!=None):
            return 0
        elif(root.left!=None and root.right==None):
            return 0
        preorder1(self,root.left)
        if(preorder2(self,root.right)==None and self.count>=len(self.data)):
            return 1
        return 0