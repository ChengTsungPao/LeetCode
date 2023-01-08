class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        Floyd Warshall => 第k次loop，確保轉運k次後，能到達的點
        '''
        
        # define the char number
        ch_to_num, num = {}, 0
        for numerator, denominator in equations:
            if numerator not in ch_to_num:
                ch_to_num[numerator] = num
                num += 1
            if denominator not in ch_to_num:
                ch_to_num[denominator] = num
                num += 1          
                
        # create Floyd Warshall init matrix
        n = len(ch_to_num)
        cost = [[1 if i == j else float("inf") for j in range(n)] for i in range(n)]
        for (numerator, denominator), value in zip(equations, values):
            i, j = ch_to_num[numerator], ch_to_num[denominator]
            cost[i][j] = value
            cost[j][i] = 1 / value
            
        # running Floyd Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if cost[i][j] == float("inf") and cost[i][k] * cost[k][j] != float("inf"):
                        cost[i][j] = cost[i][k] * cost[k][j]
                        
        # find answer
        ans = []
        for numerator, denominator in queries:
            if numerator not in ch_to_num or denominator not in ch_to_num:
                ans.append(-1.0)
            else:
                i, j = ch_to_num[numerator], ch_to_num[denominator]
                ans.append(cost[i][j] if cost[i][j] != float("inf") else -1.0)
                
        return ans