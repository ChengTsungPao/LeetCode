class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int n = prices.size();
        
        int hold = -prices[0], sell = 0;
        for(int i = 1; i < n; i++){
            int tmp = hold;
            hold = max(hold, sell - prices[i]);
            sell = max(sell, tmp + prices[i] - fee);
        }
        return sell;
    }
};