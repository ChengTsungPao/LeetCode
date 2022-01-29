class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        ans = 0        
        i = j = 0
        flipped = 0
        que = collections.deque()
        
        while j < len(nums):
            
            if nums[j] == 1:
                pass
                
            elif flipped < k:
                flipped += 1
                que.appendleft(j)
                
            else:
                if flipped > 0:
                    i = que.pop() + 1
                    que.appendleft(j)
                else:
                    i = j + 1
            
            ans = max(ans, j - i + 1)
            j += 1
            
        return ans