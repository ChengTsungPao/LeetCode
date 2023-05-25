class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        
        if(k == 0) {
            return 1;
        }
        
        double suffixSum = 0;
        vector<double> dp(k, 0);
        for(int i = k - 1; i >= 0; i--){
            if(i + maxPts > n){
                dp[i] = suffixSum / maxPts + (double)(n - k + 1) / maxPts;
            } else if (i + maxPts >= k){
                dp[i] += suffixSum / maxPts + (double)(i + maxPts - k + 1) / maxPts;
            } else {
                dp[i] += suffixSum / maxPts;
                suffixSum -= dp[i + maxPts];
            }
            suffixSum += dp[i];
        }
        
        return dp[0];
    }
};