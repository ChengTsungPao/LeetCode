class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:    
        
        MOD = pow(10, 9) + 7
        
        n = len(arr)
        
        left  = [-1] * n
        right = [ n] * n
        
        stack1 = []
        stack2 = []
        for i in range(n):
            while stack1 and stack1[-1][1] >= arr[i]:
                preI, _ = stack1.pop()
                right[preI] = i
            stack1.append((i, arr[i]))
            
            while stack2 and stack2[-1][1] > arr[~i]:
                nextI, _ = stack2.pop()
                left[nextI] = n + (~i)        
            stack2.append((n + (~i), arr[~i]))
            
        return sum([arr[i] * (right[i] - i) * (i - left[i]) for i in range(n)]) % MOD