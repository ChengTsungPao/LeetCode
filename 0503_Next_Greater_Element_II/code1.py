class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [-1] * n
        
        stack = []
        for i in range(2*n):
            i = i % n
            while stack and stack[-1][0] < nums[i]:
                _, index = stack.pop()
                ans[index] = nums[i]
                
            stack.append((nums[i], i))
            
        return ans