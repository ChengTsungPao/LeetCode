class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        status = set()
        que = collections.deque()
        que.appendleft((nums[0][0], 0, 0))
        while que:
            try:
                if((que[-1][1] + 1, que[-1][2]) not in status):
                    que.appendleft((nums[que[-1][1] + 1][que[-1][2]], que[-1][1] + 1, que[-1][2]))
                    status.add((que[-1][1] + 1, que[-1][2]))
            except:
                pass
            try:
                if((que[-1][1], que[-1][2] + 1) not in status):
                    que.appendleft((nums[que[-1][1]][que[-1][2] + 1], que[-1][1], que[-1][2] + 1))
                    status.add((que[-1][1], que[-1][2] + 1))
            except:
                pass
            ans.append(que.pop()[0])
        return ans