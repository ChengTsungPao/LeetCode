class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        
        dp = [0] * n
        dp[0] = nums[0]
        
        heap = [(-dp[0], 0)]
        
        for i in range(1, n):
            
            while heap and i - heap[0][1] > k:
                heapq.heappop(heap)
                
            dp[i] = nums[i] + (-heap[0][0])
            
            heapq.heappush(heap, (-dp[i], i))
            
        return dp[n - 1]