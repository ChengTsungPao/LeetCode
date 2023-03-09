class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        '''
        [3, 1, 2, 3, 5, 7, 5, 7]
         ^  L        R  
        
        [I, I, M, M, M, A, A, B]
        '''
        
        n = len(nums)
                
        firstMinKIndex = [-1] * n
        minKIndex = -1
        
        firstMaxKIndex = [-1] * n
        maxKIndex = -1
            
        firstInValidIndex = [-1] * n
        inValidIndex = -1

        for i in range(n - 1, -1, -1):
            num = nums[i]
            if not (minK <= num <= maxK):
                inValidIndex = i
            if num == maxK:
                maxKIndex = i
            if num == minK:
                minKIndex = i
                
            firstMinKIndex[i] = minKIndex
            firstMaxKIndex[i] = maxKIndex
            firstInValidIndex[i] = inValidIndex
        
        ans = 0
        for i, num in enumerate(nums):
            maxKIndex = firstMaxKIndex[i] if firstMaxKIndex[i] >= 0 else n
            minKIndex = firstMinKIndex[i] if firstMinKIndex[i] >= 0 else n
            inValidIndex = firstInValidIndex[i] if firstInValidIndex[i] >= 0 else n
            
            leftValidIndex = max(maxKIndex, minKIndex)
            rightValidIndex = inValidIndex - 1

            ans += rightValidIndex - leftValidIndex + 1 if rightValidIndex >= leftValidIndex else 0
                
        return ans
