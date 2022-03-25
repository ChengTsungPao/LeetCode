class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        n = len(expression)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(n):
                if expression[i: j + 1].isdigit():
                    dp[i][j] = [int(expression[i: j + 1])]
                else:
                    ans = []
                    for k in range(i, j + 1):
                        if not expression[k].isdigit():
                            for left in dp[i][k - 1]:
                                for right in dp[k + 1][j]:
                                    ans.append(eval(str(left) + expression[k] + str(right)))
                    dp[i][j] = ans
                    
        return dp[0][n - 1]