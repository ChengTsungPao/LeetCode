class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n < 3:
            return False
        
        preMin = [0] * n
        preMin[0] = nums[0]
        for i in range(1, n):
            preMin[i] = min(preMin[i - 1], nums[i])
            
        stack = []
        for j in range(n - 1, 0, -1):
            if preMin[j - 1] > nums[j]:
                continue
                
            while stack and stack[-1] <= preMin[j - 1]:
                stack.pop()
                
            if stack and stack[-1] < nums[j]:
                return True
            
            stack.append(nums[j])
            
        return False