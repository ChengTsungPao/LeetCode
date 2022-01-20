class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        vaildSubArray = collections.defaultdict(list)
        
        total = 0
        preSumIndex = collections.defaultdict(list)
        preSumIndex[0].append(-1)
        
        for index in range(len(arr)):
            total += arr[index]
            
            if total - target in preSumIndex:
                for preIndex in preSumIndex[total - target]:
                    vaildSubArray[index - preIndex].append((preIndex + 1, index))
                    
            preSumIndex[total].append(index)
        
        
        def vaildMatch(length1, length2):
            
            for i in range(len(vaildSubArray[length1])): 
                m, n = vaildSubArray[length1][i]
                
                for j in range(len(vaildSubArray[length2])):
                    m_, n_ = vaildSubArray[length2][j]
                    
                    if i == j and length1 == length2:
                        continue
                    
                    if n < m_ or n_< m:
                        return True
                    
            return False
            
            
        minLength = float("inf")
        sorted_length = sorted(vaildSubArray.keys())
        
        for length1 in sorted_length:            
            for length2 in sorted_length:
                if length1 + length2 < minLength and vaildMatch(length1, length2):
                    minLength = length1 + length2
        
        
        return minLength if minLength != float("inf") else -1