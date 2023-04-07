class Solution {
public:
    int numEnclaves(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        for(int i = 0; i < m; i++){
            recur(i, 0, grid);
            recur(i, n - 1, grid);
        }
        
        for(int j = 0; j < n; j++){
            recur(0, j, grid);
            recur(m - 1, j, grid);
        }
        
        int ans = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                ans += grid[i][j];
            }
        }
        
        return ans;
    }
    
    void recur(int i, int j, vector<vector<int>>& grid){
        int m = grid.size();
        int n = grid[0].size();
        
        if(i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == 0){
            return;
        }
        
        grid[i][j] = 0;
        
        recur(i + 1, j, grid);
        recur(i, j + 1, grid);
        recur(i - 1, j, grid);
        recur(i, j - 1, grid);
    }
    
};