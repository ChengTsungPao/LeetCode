class Solution {
public:
    int change(int amount, vector<int>& coins) {
        
        if(coins.size() == 0){
            return amount == 0;
        }

        int dp[5001][501];
        std::sort(coins.begin(), coins.end());

        for(int i = 0; i < coins.size(); i++){
            dp[0][i] = 1;
        }

        for(int i = 1; i <= amount; i++){

            dp[i][0] = i - coins[0] >= 0 && dp[i - coins[0]][0];
            
            for(int j = 1; j < coins.size() ; j++){
                
                dp[i][j] = dp[i][j - 1];
                
                if(coins[j] <= i){
                    dp[i][j] += dp[i - coins[j]][j];
                }

            }

        }

        return dp[amount][coins.size()-1];
    }
};