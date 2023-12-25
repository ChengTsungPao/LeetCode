class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        
        nums.sort()
        
        ans = []
        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append(nums[i: i + 3])
        return ans