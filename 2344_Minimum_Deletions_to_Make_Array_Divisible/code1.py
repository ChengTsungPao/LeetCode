class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
        def gcd(a, b):
            if a > b:
                return gcd(b, a)
            
            if a == 1 or b == 1:
                return 1
            elif b % a == 0:
                return a
            
            return gcd(b % a, a)

        numsDivide_gcd = numsDivide[0]
        for i in range(1, len(numsDivide)):
            numsDivide_gcd = gcd(numsDivide_gcd, numsDivide[i])
        
        count = 0
        for num in sorted(nums):
            if numsDivide_gcd % num == 0:
                return count
            count += 1
        
        return -1