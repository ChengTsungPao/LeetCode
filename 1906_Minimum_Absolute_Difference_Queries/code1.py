class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        preSum = []
        count = [0] * (100 + 1)
        for num in nums:
            count[num] += 1
            preSum.append(count.copy())
            
        def getCountArr(i, j):
            if i == 0:
                return preSum[j]
            
            currentCount = []
            for k in range(100 + 1):
                currentCount.append(preSum[j][k] - preSum[i - 1][k])
                
            return currentCount
        
        ans = []
        for i, j in queries:
            currentCount = getCountArr(i, j)
            
            min_distance = float("inf")
            preIndex = -1
            for k in range(len(currentCount)):
                if currentCount[k] > 0:
                    if preIndex >= 0:
                        min_distance = min(min_distance, k - preIndex)
                    preIndex = k
                    
            if min_distance == float("inf"):
                ans.append(-1)
            else:
                ans.append(min_distance)
                
        return ans