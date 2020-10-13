class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        def dfs(index, M, Alex, Lee, who):
            if (index, M, who) not in dp:
                if index >= len(piles):
                    return Alex, Lee
                tmp = 0, 0
                for i in range(1, 2 * M + 1):
                    if who:
                        tmpAlex, tmpLee = dfs(index + i, max(M, i), Alex + sum(piles[index : index + i]), Lee, not who)
                        if tmpAlex - Alex > tmp[0]:
                            tmp = tmpAlex - Alex, tmpLee - Lee 
                    else:
                        tmpAlex, tmpLee = dfs(index + i, max(M, i), Alex, Lee + sum(piles[index : index + i]), not who)
                        if tmpLee - Lee > tmp[1]:
                            tmp = tmpAlex - Alex, tmpLee - Lee
                    dp[index, M, who] = tmp
            return Alex + dp[index, M, who][0], Lee + dp[index, M, who][1]
        return dfs(0, 1, 0, 0, True)[0]