# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        if root == None: return ans
        que = collections.deque()
        que.appendleft((root, 0))
        while que:
            if que[-1][0].right:
                que.appendleft((que[-1][0].right, que[-1][1] + 1))
            if que[-1][0].left:
                que.appendleft((que[-1][0].left, que[-1][1] + 1))
            if que[-1][1] == len(ans):
                ans.append(que[-1][0].val)
            que.pop()
        return ans