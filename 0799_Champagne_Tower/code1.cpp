class Solution {
public:
    double dp[101][101];
    double champagneTower(int poured, int query_row, int query_glass) {
        memset(dp, 0, sizeof(dp));
        dp[0][0] = poured;
        for(int r = 0; r < query_row; r++){
            for(int c = 0; c <= r; c++){
                dp[r + 1][c] += (dp[r][c] >= 1) ? (dp[r][c] - 1) / 2 : 0;
                dp[r + 1][c + 1] += (dp[r][c] >= 1) ? (dp[r][c] - 1) / 2 : 0;
                dp[r][c] = (dp[r][c] >= 1) ? 1 : dp[r][c];
            }
            if(dp[r + 1][(r + 1) / 2] <= 1) break;
        }
        return (dp[query_row][query_glass] >= 1) ? 1: dp[query_row][query_glass];
    }
};