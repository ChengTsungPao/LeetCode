class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ans = []
        que = collections.deque()
        for i, num in enumerate(nums):
            while que and num > que[-1][0]:
                que.pop()
            que.append((num, i))
            while que and que[0][1] <= i - k:
                que.popleft()
            if i >= k - 1:
                ans.append(que[0][0])
            
        return ans