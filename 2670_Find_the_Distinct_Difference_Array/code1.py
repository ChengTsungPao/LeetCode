class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        setP, setS = set(), set()
        prefix, suffix = [0] * n, [0] * n
        
        for i in range(n):
            num = nums[i]
            setP.add(num)
            prefix[i] = len(setP)
            
            num = nums[~i]
            suffix[~i] = len(setS)
            setS.add(num)
            
        return [prefix[i] - suffix[i] for i in range(n)]