class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        def get_length(num, visited = set()):
            
            length = 0
            
            while num not in visited:
                visited.add(num)
                num = nums[num]
                length += 1
                
            return length
              
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, get_length(i))
            
        return ans
        