class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int n = nums.size();
        
        int maxLength = 0;
        vector<int> dp(n + 1, 0), dpMax(n + 1, 0);
        for(int i = 0; i < n; i++){
            dpMax[i] = 1;
            for(int j = 0; j < i; j++){
                if(nums[j] < nums[i]){
                    dpMax[i] = max(dpMax[i], dpMax[j] + 1);
                }
            }
            
            dp[i] = (dpMax[i] == 1) ? 1 : 0;
            for(int j = 0; j < i; j++){
                if(nums[j] < nums[i] && dpMax[j] + 1 == dpMax[i]){
                    dp[i] += dp[j];
                }   
            }
            maxLength = max(maxLength, dpMax[i]);
        }
        
        int ans = 0;
        for(int i = 0; i < n; i++){
            if(dpMax[i] == maxLength){
                ans += dp[i];
            }
        }
        
        return ans;
    }
};