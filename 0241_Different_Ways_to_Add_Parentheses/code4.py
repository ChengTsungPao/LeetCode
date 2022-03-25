class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        memo = {}
        def recur(i, j):
            
            if (i, j) not in memo:
                
                if expression[i: j + 1].isdigit():
                    return [int(expression[i: j + 1])]

                ret = []
                for k in range(i, j + 1):
                    if not expression[k].isdigit():
                        for left in recur(i, k - 1):
                            for right in recur(k + 1, j):
                                ret.append(eval(str(left) + expression[k] + str(right)))
                                
                memo[i, j] = ret
                            
            return memo[i, j]
        
        return recur(0, len(expression) - 1)