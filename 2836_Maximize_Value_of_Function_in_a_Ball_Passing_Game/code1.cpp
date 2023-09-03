class Solution {
public:
    
    long long getMaxFunctionValue(vector<int>& receiver, long long k) {
        int n = receiver.size(), m = log2(k);
        vector<vector<tuple<int, long long>>> dp(n + 1, vector<tuple<int, long long>>(m + 1, {-1, -1}));
        
        for(int x = 0; x < n; x++){
            int sum = receiver[x];
            int nextX = receiver[x];
            dp[x][0] = {nextX, sum};
        }
        
        for(int i = 1; i <= m; i++){
            for(int x1 = 0; x1 < n; x1++){
                int x2 = get<0>(dp[x1][i - 1]);
                int x3 = get<0>(dp[x2][i - 1]);
                long long sum2 = get<1>(dp[x1][i - 1]);
                long long sum3 = get<1>(dp[x2][i - 1]);
                if(x3 != -1){
                    dp[x1][i] = {x3, sum2 + sum3};
                }
            }
        }
        
        long long ans = 0;
        for(int x = 0; x < n; x++){
            int curX = x;
            long long sum = x;
            for(int i = 0; i <= m; i++){
                if((k >> i & 1) == 1){
                    int nextX = get<0>(dp[curX][i]);
                    long long nextSum = get<1>(dp[curX][i]);
                    sum += nextSum;
                    curX = nextX;
                }
            }
            ans = max(ans, sum);
        }
        
        return ans;       
    }
};