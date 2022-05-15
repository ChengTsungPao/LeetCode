class Solution:
    def numTilings(self, n: int) -> int:
        
        # 以 "1、2、3、4、5...n" n種長度為基礎組成長度無n的長方形 (2只算橫的避免重複計算)

        MOD = 10 ** 9 + 7
        
        perm = [1] * (n + 1)
        for i in range(1, n + 1):
            perm[i] = perm[i - 1] * i
        
        def calculate(countKind):
            total = sum(countKind)
            totalKind = perm[total]
            
            combKind = 1
            for count in countKind:
                combKind *= perm[count]
            combKind = totalKind // combKind
            combKind %= MOD
            
            return (combKind * pow(2, sum(countKind[2:]), MOD)) % MOD
        
        memo = {}
        def recur(target, coin):
            
            if (target, coin) not in memo:
            
                if target == 0:
                    return [[0] * (n - coin + 1)]
                elif target < 0 or coin > n:
                    return []

                ans = []
                for i in range(target // coin + 1):
                    for ret in recur(target - coin * i, coin + 1):
                        ans.append([i] + ret)

                memo[target, coin] = ans
            
            return memo[target, coin]
        
        ans = 0
        for combKind in recur(n, 1):
            ans += calculate(combKind)
            ans %= MOD
            
        return ans