class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        n = len(nums)
        
        # firstLen所有subarray的總和、prefixMax和suffixMax
        firstSum = [sum(nums[:firstLen])]
        for index in range(firstLen, n):
            firstSum.append(firstSum[-1] + nums[index] - nums[index - firstLen])
            
        firstPrefixMax = [firstSum[0]]
        for index in range(1, n - firstLen):
            firstPrefixMax.append(max(firstPrefixMax[-1], firstSum[index]))
            
        firstSuffixMax = [firstSum[-1]]
        for index in range(1, n - firstLen):
            firstSuffixMax.append(max(firstSuffixMax[-1], firstSum[~index]))  
        firstSuffixMax.reverse()
        
        # secondLen所有subarray的總和
        secondSum = [sum(nums[:secondLen])]
        for index in range(secondLen, n):
            secondSum.append(secondSum[-1] + nums[index] - nums[index - secondLen])

        # firstLen和secondLen的subarray最大總和
        ans = 0
        for index in range(n - secondLen + 1):
            if index >= firstLen:
                ans = max(ans, firstPrefixMax[index - firstLen] + secondSum[index])
            if index + secondLen < n - firstLen:
                ans = max(ans, firstSuffixMax[index + secondLen] + secondSum[index])
                
        return ans