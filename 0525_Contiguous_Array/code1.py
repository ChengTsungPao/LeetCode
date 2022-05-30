class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        ans = 0
        count = {0: -1}
        zero = one = 0

        for i, num in enumerate(nums):
            zero += num == 0
            one += num == 1
            
            if zero - one in count:
                ans = max(ans, i - count[zero - one])
            else:
                count[zero - one] = i

        return ans