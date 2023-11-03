class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        count1 = sum1 = 0
        for num1 in nums1:
            count1 += num1 == 0
            sum1 += num1
        
        count2 = sum2 = 0
        for num2 in nums2:
            count2 += num2 == 0
            sum2 += num2
            
        if count1 == 0 and sum2 + count2 > sum1:
            return -1
        elif count2 == 0 and sum1 + count1 > sum2:
            return -1
            
        return max(sum1 + count1, sum2 + count2)