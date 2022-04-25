class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        def isNoneDecrease(nums):
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True
        
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                ans = False
                num1, num2 = nums[i], nums[i + 1]
                nums[i] = nums[i + 1] = num1
                ans = ans or isNoneDecrease(nums)
                nums[i] = nums[i + 1] = num2
                ans = ans or isNoneDecrease(nums)
                return ans
                
        return True