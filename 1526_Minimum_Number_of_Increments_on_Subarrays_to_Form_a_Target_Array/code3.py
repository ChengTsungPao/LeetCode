class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        '''
            _     _
         >_|_| > |_|    _
        >|_|_|_>_|_|_>_|_|
        >|_|_|_|_|_|_|_|_|
        
        '''
        return target[0] + sum([max(target[i] - target[i - 1], 0) for i in range(1, len(target))])