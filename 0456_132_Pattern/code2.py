class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        # 概念: 每次決定的"nums[k]"都是最佳選擇 (將近"nums[j]"的數值)
        # Step1: 用"Monotonic Stack"決定好"nums[k]"和"nums[j]" (nums[k] < nums[j])
        # Step2: 一個一個測試 => nums[i] < nums[k]
        
        stack = []             # decrease => candidate of nums[k]
        num_k = -float("inf")  # decide nums[k] 
        
        for i in range(len(nums) - 1, -1, -1):
            
            num_i = nums[i]
            if num_i < num_k:
                return True
            
            num_j = nums[i]
            while stack and stack[-1] < num_j:
                num_k = stack.pop()
                
            stack.append(nums[i])
            
        return False