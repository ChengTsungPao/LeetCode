class Solution {
public:
    int MOD = pow(10, 9) + 7;
    
    int countPaths(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        int ans = 0;
        vector<vector<int>> count(m, vector<int>(n, -1));
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                ans = (ans + recur(i, j, 0, count, grid)) % MOD;
            }
        }
        
        return ans;
    }
    
    int recur(int i, int j, int pre, vector<vector<int>>& count, vector<vector<int>>& grid){
        int m = grid.size();
        int n = grid[0].size();
        
        if(i >= m || i < 0 || j >= n || j < 0 || pre >= grid[i][j]) {
            return 0;
        }
        
        if(count[i][j] != -1){
            return count[i][j];
        }
        
        int ans = 1;
        
        ans = (ans + recur(i + 1, j, grid[i][j], count, grid)) % MOD;
        ans = (ans + recur(i, j + 1, grid[i][j], count, grid)) % MOD;
        ans = (ans + recur(i - 1, j, grid[i][j], count, grid)) % MOD;
        ans = (ans + recur(i, j - 1, grid[i][j], count, grid)) % MOD;
        
        count[i][j] = ans;
        return ans;
    }
};