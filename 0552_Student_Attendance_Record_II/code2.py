class Solution:
    def checkRecord(self, n: int) -> int:
        
        MOD = 10 ** 9 + 7
        
        # state[A, L]
        state = collections.defaultdict(int)
        
        state[0, 0] = 1
        state[0, 1] = 1
        state[0, 2] = 1
        state[1, 0] = 1
        state[1, 1] = 1
        state[1, 2] = 1
        
        for _ in range(n - 1, -1, -1):
            prevState = collections.defaultdict(int)
            
            # nextState  =>    P             A             L
            prevState[0, 0] = (state[0, 0] + state[0, 1] + state[1, 0]) % MOD
            prevState[0, 1] = (state[0, 0] + state[0, 2] + state[1, 0]) % MOD
            prevState[0, 2] = (state[0, 0] + state[0, 3] + state[1, 0]) % MOD
            prevState[1, 0] = (state[1, 0] + state[2, 0] + state[1, 1]) % MOD
            prevState[1, 1] = (state[1, 0] + state[2, 0] + state[1, 2]) % MOD
            prevState[1, 2] = (state[1, 0] + state[2, 0] + state[1, 3]) % MOD
            
            state = prevState
        
        return state[0, 0]