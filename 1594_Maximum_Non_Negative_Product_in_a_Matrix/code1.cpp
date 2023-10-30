class Solution {
public:
    int maxProductPath(vector<vector<int>>& grid) {
        int M = pow(10, 9) + 7;
        int m = grid.size();
        int n = grid[0].size();
        
        vector<vector<long long>> dp_p(m, vector<long long>(n, -1));
        vector<vector<long long>> dp_n(m, vector<long long>(n, -1));
        
        dp_p[0][0] = grid[0][0];
        dp_n[0][0] = grid[0][0];
        for(int i = 1; i < m; i++){
            dp_p[i][0] = dp_p[i - 1][0] * grid[i][0];
            dp_n[i][0] = dp_p[i][0];
        }
        
        for(int j = 1; j < n; j++){
            dp_p[0][j] = dp_p[0][j - 1] * grid[0][j];
            dp_n[0][j] = dp_p[0][j];
        }

        for(int i = 1; i < m; i++){
            for(int j = 1; j < n; j++){
                int val = grid[i][j];
                if(val >= 0){
                    dp_p[i][j] = max(dp_p[i - 1][j], dp_p[i][j - 1]) * val;
                    dp_n[i][j] = min(dp_n[i - 1][j], dp_n[i][j - 1]) * val;
                } else {
                    dp_p[i][j] = min(dp_n[i - 1][j], dp_n[i][j - 1]) * val;
                    dp_n[i][j] = max(dp_p[i - 1][j], dp_p[i][j - 1]) * val;
                }
            }
        }
        return (dp_p[m - 1][n - 1] < 0) ? -1 : dp_p[m - 1][n - 1] % M;
    }
};