class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        '''
        [3, 4, 5, 1, 2]
        [V, X, X, O, O]
            O, O, X, X
            O, X, O, X
            X, O, X, O
            X, O, O, X
            O, X, X, O
        '''
        
        MOD = pow(10, 9) + 7
        
        def recur(nums):
            n = len(nums)
            if n <= 1:
                return 1
            
            rootNum = nums[0]
            left, right = [], []
            for i in range(1, n):
                num = nums[i]
                if num < rootNum:
                    left.append(num)
                else:
                    right.append(num)
            
            k = len(left)
            return math.comb(n - 1, k) * recur(left) * recur(right)
        
        return (recur(nums) - 1) % MOD