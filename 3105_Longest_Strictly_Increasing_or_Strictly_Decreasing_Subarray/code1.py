class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 1
        i, j = 0, 1
        while j < n and nums[i] == nums[j]:
            i += 1
            j += 1
        if j >= n:
            return ans
        isIncr = nums[i] < nums[j]
        
        while j < n:             
            if nums[j - 1] < nums[j]:
                if isIncr:
                    j += 1
                else:
                    ans = max(ans, j - i)
                    i = j - 1
                    isIncr = not isIncr
            elif nums[j - 1] > nums[j]:
                if not isIncr:
                    j += 1
                else:
                    ans = max(ans, j - i)
                    i = j - 1
                    isIncr = not isIncr
            else:
                ans = max(ans, j - i)
                i = j
                j += 1
                while j < n and nums[i] == nums[j]:
                    i += 1
                    j += 1
                if j >= n:
                    return ans
                isIncr = nums[i] < nums[j]
            
        ans = max(ans, j - i)
            
        return ans