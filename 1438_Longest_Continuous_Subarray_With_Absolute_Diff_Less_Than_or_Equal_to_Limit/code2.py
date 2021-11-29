class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        ans = 1
        
        maxHeap = [(-nums[0], 0)]
        minHeap = [(nums[0], 0)]
        
        i, j = 0, 1
        
        while j < len(nums):
            
            heapq.heappush(maxHeap, (-nums[j], j))
            heapq.heappush(minHeap, (nums[j], j))
            
            while -maxHeap[0][0] - minHeap[0][0] > limit:
                i = min(maxHeap[0][1], minHeap[0][1])

                while maxHeap[0][1] <= i:
                    heapq.heappop(maxHeap)
                    
                while minHeap[0][1] <= i:
                    heapq.heappop(minHeap)
                    
                i += 1
                
            ans = max(ans, j - i + 1)
            
            j += 1
  
        return ans