class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1, n+1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
        
        memo = {}
        def recur(i, cut):
            
            if (i, cut) not in memo:
                
                if cut == 0:
                    return preSum[n] - preSum[i]
                
                ans = float("inf")
                left = i + 1
                right = n - cut + 1
                
                while left < right:
                    mid = left + (right - left) // 2
                    
                    leftPartValue = preSum[mid] - preSum[i]
                    rightPartValue = recur(mid, cut - 1)
                    
                    ans = min(ans, max(leftPartValue, rightPartValue))
                    if leftPartValue <= rightPartValue:
                        left = mid + 1
                    else:
                        right = mid
                    
                memo[i, cut] = ans
                
            return memo[i, cut]
        
        return recur(0, m - 1)