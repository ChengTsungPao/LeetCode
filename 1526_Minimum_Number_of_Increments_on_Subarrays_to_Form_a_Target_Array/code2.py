class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        # 概念1: 每次都拿區間最小的數值來對區間內的每個數值相減 (greedy)
        # 概念2: 以greedy的觀點來說，必定是附近比我小的數值先被處理
        
        n = len(target)
        
        stack1 = []
        stack2 = []
        
        L_smallers = [0] * n
        R_smallers = [0] * n
        
        for i in range(n):
            
            while stack1 and stack1[-1][0] >= target[i]:
                _, L_i = stack1.pop()
                R_smallers[L_i] = target[i]
            stack1.append((target[i], i))    
        
            while stack2 and stack2[-1][0] > target[~i]:
                _, R_i = stack2.pop()
                L_smallers[R_i] = target[~i]
            stack2.append((target[~i], ~i))

        return sum([target[i] - max(L_smallers[i], R_smallers[i]) for i in range(n)])
