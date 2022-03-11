class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        n = len(piles)

        memo = {}
        def recur(index, M, who):
            if (index, M, who) not in memo:

                if index >= n:
                    return 0, 0

                if who:
                    ret = 0, 0
                    score = -float("inf")
                    for x in range(1, 2 * M + 1):
                        Alex, Bob = recur(index + x, max(M, x), not who)
                        Alex += sum(piles[index: index + x])
                        if Alex - Bob > score:
                            ret = Alex, Bob
                            score = Alex - Bob
                else:
                    ret = 0, 0
                    score = float("inf")
                    for x in range(1, 2 * M + 1):
                        Alex, Bob = recur(index + x, max(M, x), not who)
                        Bob += sum(piles[index: index + x])
                        if Alex - Bob < score:
                            ret = Alex, Bob
                            score = Alex - Bob

                memo[index, M, who] = ret

            return memo[index, M, who]

        return recur(0, 1, True)[0]