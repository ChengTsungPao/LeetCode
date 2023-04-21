class Solution {
public:
    int MOD = pow(10, 9) + 7;
    
    int profitableSchemes(int n, int minProfit, vector<int>& group, vector<int>& profit) {
        int m = profit.size();
        vector<vector<vector<int>>> dp(m + 1, vector<vector<int>>(n + 1, vector<int>(minProfit + 1, -1)));
        for(int i = m; i >= 0; i--){
            for(int j = 0; j <= n; j++){
                for(int k = 0; k <= minProfit; k++){
                    if(i >= m){
                        dp[i][j][k] = k == 0;
                    } else if (j - group[i] < 0){
                        dp[i][j][k] = dp[i + 1][j][k] % MOD;
                    } else {
                        dp[i][j][k] = (dp[i + 1][j][k] + dp[i + 1][j - group[i]][max(k - profit[i], 0)]) % MOD;
                    }
                }
            }
        }
        return dp[0][n][minProfit];
    }
    
};