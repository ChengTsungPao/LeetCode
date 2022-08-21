class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        n = len(nums)
        m = len(l)
        
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
            
        ans = []
        for left, right in zip(l, r):
            _sum = preSum[right + 1] - preSum[left]
            
            # optimal => segment tree: O(logn)
            subarray = nums[left: right + 1]
            start, end = min(subarray), max(subarray)
            length = right - left + 1
            
            # check sum valid
            if (start + end) * length != _sum * 2:
                ans.append(False)
                continue
            
            # check num in subarray
            subarray = set(subarray)
            if end - start == 0:
                ans.append(True)
                continue
                
            isValid = True
            for val in range(start, end + 1, (end - start) // (length - 1)):
                if val not in subarray:
                    isValid = False
                    break
                    
            ans.append(isValid)
            
        return ans