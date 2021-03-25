class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def arithmetic(sequence):
            sequence.sort()
            distance = sequence[1] - sequence[0]
            for i in range(1, len(sequence) - 1):
                if sequence[i + 1]  - sequence[i] != distance:
                    return False
            return True
        
        ans = []
        for i in range(len(l)):
            ans.append(arithmetic(nums[l[i]: r[i] + 1]))
            
        return ans