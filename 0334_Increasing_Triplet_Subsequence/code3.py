class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        # 利用 Monotonic Stack "找出j前面有沒有比較小的i"和"j後面有沒有比較大的k"
        
        n = len(nums)
        ans = [False] * n
        
        stack = []
        for k in range(n):
            
            while stack and stack[-1][0] < nums[k]:
                _, index = stack.pop()
                ans[index] = True
                
            stack.append((nums[k], k))
            
        stack = []
        for i in range(n - 1, -1, -1):
            
            while stack and stack[-1][0] > nums[i]:
                _, index = stack.pop()
                if ans[index]:
                    return True
                
            stack.append((nums[i], i))
            
        return False