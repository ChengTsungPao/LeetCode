class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        def get_length(num):
            
            length = 0
            
            while nums[num] != "#":
                num, preNum = nums[num], num
                nums[preNum] = "#"
                length += 1
                
            return length
              
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, get_length(i))
            
        return ans
        