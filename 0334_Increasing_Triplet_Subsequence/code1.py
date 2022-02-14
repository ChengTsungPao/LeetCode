class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        # Patient Sort => Longest Increasing Subsequence (LIS)
        
        arr = []
        
        for num in nums:
            index = bisect.bisect_left(arr, num)
            
            if index >= len(arr):
                arr.append(num)
                if len(arr) == 3:
                    return True
            else:
                arr[index] = num
                
        return False