class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        from sortedcontainers import SortedList
        
        MOD = pow(10, 9) + 7
        
        n = len(nums)
        
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
        
        ans = _sum = 0
        bst = SortedList([0])
        for i, num in enumerate(nums):
            _sum += num
            ans += len(bst) - bst.bisect_right(-_sum)
            bst.add(-_sum)
            
        return ans % MOD