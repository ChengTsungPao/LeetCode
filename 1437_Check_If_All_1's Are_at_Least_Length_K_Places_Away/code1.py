class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if nums == []:
            return False
        count = (nums[0] == 0) * 1
        for i in range(1, len(nums)):
            if nums[i] == 1:
                if count < k:
                    return False
                count = 0
            else:
                count += 1
        return True