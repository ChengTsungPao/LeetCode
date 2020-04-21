# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if(root == None):
            return ans
        que = collections.deque()
        que.append((root, 0))
        while que:
            if(que[-1][0].left != None):
                que.insert(0, (que[-1][0].left, que[-1][1] + 1))
            if(que[-1][0].right != None):
                que.insert(0, (que[-1][0].right, que[-1][1] + 1))
            if(len(ans) <= que[-1][1]):
                ans.append([que.pop()[0].val])
            else:
                if(que[-1][1] % 2):
                    ans[que[-1][1]].insert(0, que.pop()[0].val)
                else:
                    ans[que[-1][1]].append(que.pop()[0].val)      
        return ans