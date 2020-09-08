class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        status = set()
        for num in nums:
            if num in status:
                ans += [num]
            else:
                status.add(num)
        return ans