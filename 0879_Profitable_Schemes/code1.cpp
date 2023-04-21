class Solution {
public:
    int MOD = pow(10, 9) + 7;
    
    int profitableSchemes(int n, int minProfit, vector<int>& group, vector<int>& profit) {
        vector<vector<vector<int>>> memo(profit.size() + 1, vector<vector<int>>(n + 1, vector<int>(minProfit + 1, -1)));
        return recur(0, n, minProfit, group, profit, memo);
    }
    
    int recur(int idx, int n, int minProfit, vector<int>& group, vector<int>& profit, vector<vector<vector<int>>>& memo) {
        if(n < 0){
            return 0;
        } else if (idx >= profit.size()){
            return minProfit == 0;
        }
        
        if(memo[idx][n][minProfit] != -1){
            return memo[idx][n][minProfit];
        }
        
        int g = group[idx], p = profit[idx];
        int ans = (recur(idx + 1, n, minProfit, group, profit, memo) + recur(idx + 1, n - g, max(minProfit - p, 0), group, profit, memo)) % MOD;
        memo[idx][n][minProfit] = ans;
        return ans;
    }
    
};