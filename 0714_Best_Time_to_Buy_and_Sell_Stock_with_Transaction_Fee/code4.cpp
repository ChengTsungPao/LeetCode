class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int n = prices.size();
        vector<vector<int>> memo(n, vector<int>(2, -1));
        return recur(0, false, memo, prices, fee);
    }
    
    int recur(int idx, bool isHold, vector<vector<int>>& memo, vector<int>& prices, int fee){
        int n = prices.size();
        
        if(idx >= n){
            return 0;
        }
        
        if(memo[idx][isHold] != -1){
            return memo[idx][isHold];
        }
        
        int ans = INT_MIN;
        if(isHold){
            ans = max(prices[idx] - fee + recur(idx + 1, false, memo, prices, fee), recur(idx + 1, true, memo, prices, fee));
        } else {
            ans = max(-prices[idx] + recur(idx + 1, true, memo, prices, fee), recur(idx + 1, false, memo, prices, fee));
        }
        
        memo[idx][isHold] = ans;
        return ans;
    }
    
};