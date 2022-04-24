class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def recur(index):
            if index == len(nums):
                return [[]]
            
            ans = []
            for ret in recur(index + 1):
                ans.append(ret)
                ans.append([nums[index]] + ret)
                
            return ans
        
        return recur(0)