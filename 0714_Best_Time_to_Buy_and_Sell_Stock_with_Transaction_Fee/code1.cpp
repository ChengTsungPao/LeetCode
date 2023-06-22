class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int n = prices.size();

        vector<int> dp(n, 0);
        for(int i = 1; i < n; i++){
            dp[i] = dp[i - 1];
            for(int j = 0; j < i; j++){
                dp[i] = max(dp[i], (prices[i] - prices[j] - fee) + ((j > 0) ? dp[j - 1] : 0));
            }
        }
        return dp[n - 1];
    }
};