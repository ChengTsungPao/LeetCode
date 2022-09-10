class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        
        dp = [0] * n
        dp[0] = nums[0]
        
        que = collections.deque([(dp[0], 0)])
        
        for i in range(1, n):

            if i - k - 1 >= que[0][1]:
                que.popleft()
            
            dp[i] = nums[i] + que[0][0]
            
            while que and dp[i] >= que[-1][0]:
                que.pop()
                
            que.append((dp[i], i))
            
        return dp[n - 1]