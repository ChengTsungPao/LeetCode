class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def divid_and_conquer(i, j):
            if i == j:
                return nums[i]
            
            k = (i + j) // 2
            maxi = divid_and_conquer(i, k)
            maxj = divid_and_conquer(k + 1, j)
            
            maxL = -float("inf")
            _sum = 0
            for idx in range(k, i - 1, -1):
                _sum += nums[idx]
                maxL = max(maxL, _sum)
                
            maxR = -float("inf")
            _sum = 0
            for idx in range(k + 1, j + 1):
                _sum += nums[idx]
                maxR = max(maxR, _sum)
                
            maxk = maxL + maxR
            return max(maxi, maxj, maxk)
        
        return divid_and_conquer(0, len(nums) - 1)