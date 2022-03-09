class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)
        
        ans = 0
        visited = {}
        for i in range(len(preSum)):
            sum_ = preSum[i]
            if sum_ - k in visited:
                ans = max(ans, i - visited[sum_ - k])
            
            if sum_ not in visited:
                visited[sum_] = i
            
        return ans