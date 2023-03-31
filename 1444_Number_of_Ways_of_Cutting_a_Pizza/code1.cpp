class Solution {
public:
    int MOD = pow(10, 9) + 7;
    
    int ways(vector<string>& pizza, int k) {
        
        int m = pizza.size();
        int n = pizza[0].size();
        
        vector<vector<int>> preSum(m + 1, vector<int>(n + 1, 0));
        for(int i = 1; i <= m; i++){
            for(int j = 1; j <= n; j++){
                int isApple = (pizza[i - 1][j - 1] == 'A') ? 1 : 0;
                preSum[i][j] = isApple + preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1];
            }
        }
        
        vector<vector<vector<int>>> memo(m, vector<vector<int>>(n, vector<int>(k, -1)));
        return recur(0, 0, k - 1, preSum, memo);
    }
    
    int recur(int i, int j, int cut, vector<vector<int>>& preSum, vector<vector<vector<int>>>& memo){
        
        if(memo[i][j][cut] != -1){
            return memo[i][j][cut];
        }
        
        int m = preSum.size() - 1;
        int n = preSum[0].size() - 1;
        int remaiderApple = preSum[m][n] - preSum[i][n] - preSum[m][j] + preSum[i][j];
                
        if(cut == 0){
            return (remaiderApple > 0) ? 1 : 0;
        } else if(remaiderApple == 0){
            return 0;
        }
        
        int ans = 0;
        
        for(int r = i; r < m; r++){
            int upperApple = preSum[r + 1][n] - preSum[r + 1][j] - preSum[i][n] + preSum[i][j];
            int lowerApple = preSum[m][n] - preSum[m][j] - preSum[r + 1][n] + preSum[r + 1][j];
            if(upperApple > 0 && lowerApple > 0){
                ans += recur(r + 1, j, cut - 1, preSum, memo) % MOD;
                ans %= MOD;
            }
            
        }
        
        for(int c = j; c < n; c++){
            int upperApple = preSum[m][c + 1] - preSum[m][j] - preSum[i][c + 1] + preSum[i][j];
            int lowerApple = preSum[m][n] - preSum[m][c + 1] - preSum[i][n] + preSum[i][c + 1];
            if(upperApple > 0 && lowerApple > 0){
                ans += recur(i, c + 1, cut - 1, preSum, memo) % MOD;
                ans %= MOD;
            }
        }
        
        memo[i][j][cut] = ans;
        return ans;
    }
};