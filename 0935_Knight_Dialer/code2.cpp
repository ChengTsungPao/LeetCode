class Solution {
public:
    int knightDialer(int n) {
        
        int MOD = pow(10, 9) + 7;
        
        vector<vector<int>> nextDigitTable = {
            {4, 6},
            {6, 8}, 
            {7, 9},
            {4, 8},
            {0, 3, 9}, 
            {},
            {0, 1, 7},
            {2, 6},
            {1, 3},
            {2, 4}
        };
        
        vector<int> dp(10, 1);
        
        for(int i = 1; i < n; i++){    
            vector<int> newDp(10, 0);
            for(int digit = 0; digit < 10; digit++){
                for(int nextDigit: nextDigitTable[digit]){
                    newDp[nextDigit] = (newDp[nextDigit] + dp[digit]) % MOD;
                }
            }
            dp = newDp;
        }
        
        int ans = 0;
        for(int count: dp){
            ans = (ans + count) % MOD;
        }
        
        return ans;
    }
};