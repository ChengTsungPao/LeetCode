class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        
        def recur(index):
            if index >= len(nums):
                return set([0])

            ans = set()
            for s in recur(index + 1):
                ans.add(s)
                ans.add(nums[index] + s)
                
            return ans
        
        return target in recur(0)