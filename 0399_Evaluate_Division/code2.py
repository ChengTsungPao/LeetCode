class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        Floyd Warshall => 第k次loop，確保轉運k次後，能到達的點
        '''
        
        cur_number = 0
        number = {}
        
        for end, start in equations:
            if start not in number:
                number[start] = cur_number
                cur_number += 1

            if end not in number:
                number[end] = cur_number
                cur_number += 1
        
        
        n = len(number)
        dp = [[1 if i == j else -1 for j in range(n)] for i in range(n)]

        for i in range(len(equations)):
            endNum = number[equations[i][0]]
            startNum = number[equations[i][1]]
            value = values[i]
            dp[startNum][endNum] = value
            dp[endNum][startNum] = 1 / value
           
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][j] == -1 and dp[i][k] > 0 and dp[k][j] > 0:
                        dp[i][j] = dp[i][k] * dp[k][j]
                        

        ans = []
        for end, start in queries:
            if end in number and start in number:
                endNum = number[end]
                startNum = number[start]    
                ans.append(dp[startNum][endNum])
            else:
                ans.append(-1)
        
        return ans