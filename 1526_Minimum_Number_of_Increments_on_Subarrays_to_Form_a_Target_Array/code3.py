class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        '''
            _     _
         >_|_| > |_|    _
        >|_|_|_>_|_|_>_|_|
        >|_|_|_|_|_|_|_|_|
         [2,3,1,1,3,1,1,2]
        
        '''
        return target[0] + sum([max(target[i] - target[i - 1], 0) for i in range(1, len(target))])