class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        '''
        Recursion min-max
            Alice => max((Alice - Bob) + getScore)
            Bob   => min((Alice - Bob) - getScore)
        Recursion max
            Alice => max(getScore - (Bob - Alice)) = max((Alice + getScore) - Bob)
            Bob   => max(getScore - (Alice - Bob)) = max((Bob + getScore) - Alice)
        Recursion min
            Alice => min((Bob - Alice) + getScore) = min((Bob + getScore) - Alice)
            Bob   => min((Alice - Bob) + getScore) = min((Alice + getScore) - Bob)
        '''
        
        memo = {}
        def recur(i, j):
            if (i, j) not in memo:

                if i > j:
                    return 0

                memo[i, j] = max(piles[i] - recur(i + 1, j), piles[j] - recur(i, j - 1))

            return memo[i, j]

        return recur(0, len(piles) - 1) >= 0