class Solution {
public:
    int maximizeWin(vector<int>& prizePositions, int k) {        
        int n = prizePositions.size();
        
        int ans = 1, i = 0;
        vector<int> dp(n, 1);
        for(int j = 1; j < n; j++){
            while(prizePositions[j] - prizePositions[i] > k) i++;
            dp[j] = max(dp[j - 1], j - i + 1);
            ans = max(ans, ((i > 0) ? dp[i - 1] : 0) + (j - i + 1));
        }
        return ans;
    }
};