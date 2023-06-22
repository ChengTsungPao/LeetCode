class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        /*         
        dp[i] = max(dp[i - 1], max((prices[i] - prices[j] - fee) + dp[j - 1], j = 0 ~ i - 1))
              = max(dp[i - 1], max(f(i, j), j = 0 ~ i - 1))
        
        f(i, j) = prices[i] - prices[j] - fee) + dp[j - 1] 
                = prices[i] + (-prices[j] - fee + dp[j - 1]) = g(i) + h(j)
        */
        
        int n = prices.size();
        
        int maxj = -prices[0] - fee;
        vector<int> dp(n, 0);
        for(int i = 1; i < n; i++){
            dp[i] = max(dp[i - 1], prices[i] + maxj);
            maxj = max(maxj, -prices[i] - fee + dp[i - 1]);
        }
        return dp[n - 1];
    }
};