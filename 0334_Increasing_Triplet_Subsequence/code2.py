class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        # 策略 => 找最小和次小的在往後找比較有機會
        
        first_small_num = float("inf")
        second_small_num = float("inf")
        
        for num in nums:
            if num <= first_small_num:
                first_small_num = num
            elif num <= second_small_num:
                second_small_num = num
            else:
                return True
                
        return False