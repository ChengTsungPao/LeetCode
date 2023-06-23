class Solution {
public:
    int longestArithSeqLength(vector<int>& nums) {
        int n = nums.size();
        
        int shift = 500;
        int dp[n][1001];
        memset(dp, 0, sizeof(dp));
        
        int ans = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < i; j++){
                int d = nums[i] - nums[j] + shift;
                dp[i][d] = max(dp[i][d], dp[j][d] + 1);
                ans = max(ans, dp[i][d]);
            }
        }
        return ans + 1;
    }
};