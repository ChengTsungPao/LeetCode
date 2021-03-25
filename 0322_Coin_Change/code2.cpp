class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int dp[10001] = {0};
        std::sort(coins.begin(), coins.end());

        for(int i = 1; i <= amount; i++){
            dp[i] = INT_MAX;   

            for(int j = 0; j < coins.size() && coins[j] <= i; j++){
                dp[i] = min(dp[i], dp[i - coins[j]]);
            }
            
            dp[i] += dp[i] != INT_MAX;
        }

        if(dp[amount] == INT_MAX){
            return -1;
        }else{
            return dp[amount]; 
        }
    }
};