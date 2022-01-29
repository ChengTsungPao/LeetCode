class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
    
        def recur(expression, memo = {}):
            if expression not in memo:
            
                if expression.isdigit():
                    return [int(expression)]

                ans = []
                for i in range(len(expression)):
                    if not expression[i].isdigit():
                        for num1 in recur(expression[:i]):
                            for num2 in recur(expression[i + 1:]):
                                ans.append(eval(str(num1) + expression[i] + str(num2)))
                                
                memo[expression] = ans
                            
            return memo[expression]
        
        return recur(expression)
