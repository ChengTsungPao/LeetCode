class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        
        isPalindromic = lambda x: str(x) == str(x)[::-1]
        
        nums.sort()
        mid = nums[n // 2]
        
        lower = mid
        while not isPalindromic(lower): 
            lower -= 1
            
        upper = mid
        while not isPalindromic(upper): 
            upper += 1
            
        return min(
            sum([abs(num - lower) for num in nums]),
            sum([abs(num - upper) for num in nums])
        )