class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        dp = [[]]
        for num in nums:
            newDp = []
            for subset in dp:
                newDp.append(subset)
                newDp.append(subset + [num])
            dp = newDp
                
        return dp