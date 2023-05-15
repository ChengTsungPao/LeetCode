class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        
        ans, nums = [], [0] * n
        
        adjacent = 0
        for index, color in queries:
            if nums[index] > 0:
                adjacent -= nums[index] == nums[index - 1] if index - 1 >= 0 else 0
                adjacent -= nums[index] == nums[index + 1] if index + 1 <  n else 0
                
            nums[index] = color
            adjacent += nums[index] == nums[index - 1] if index - 1 >= 0 else 0
            adjacent += nums[index] == nums[index + 1] if index + 1 <  n else 0
            
            ans.append(adjacent)
        
        return ans