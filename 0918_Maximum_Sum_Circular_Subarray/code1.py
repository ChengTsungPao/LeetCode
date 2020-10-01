class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        A.insert(0, 0)
        for i in range(1, len(A)):
            A[i] += A[i - 1]
            
        AnsMax = -float("inf")
        tempMin = (0, A[0])
        
        AnsMin = float("inf")
        tempMax = (0, A[0])
        for i in range(len(A) - 1):
            if A[i] < tempMin[1]:
                tempMin = (i, A[i])
            if A[i + 1] - tempMin[1] > AnsMax:
                AnsMax = A[i + 1] - tempMin[1]
    
            if A[i] > tempMax[1]:
                tempMax = (i, A[i])
            if A[i + 1] - tempMax[1] < AnsMin:
                AnsMin = A[i + 1] - tempMax[1]
                
        if A[-1] == AnsMin:
            return AnsMax
        else:
            return max(AnsMax, A[-1] - AnsMin)