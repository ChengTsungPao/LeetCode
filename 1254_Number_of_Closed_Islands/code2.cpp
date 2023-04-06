class Solution {
public:
    int closedIsland(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        int ans = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 0 && recur(i, j, grid)){
                    ans += 1;
                }
            }
        }
        
        return ans;
    }
    
    bool recur(int i, int j, vector<vector<int>>& grid){
        int m = grid.size();
        int n = grid[0].size();
        
        if(i < 0 || i >= m || j < 0 || j >= n){
            return false;
        }
        
        if(grid[i][j] == 1){
            return true;
        }
        
        grid[i][j] = 1;
        
        bool isClosed = true;
        isClosed = recur(i + 1, j, grid) && isClosed;
        isClosed = recur(i, j + 1, grid) && isClosed;
        isClosed = recur(i - 1, j, grid) && isClosed;
        isClosed = recur(i, j - 1, grid) && isClosed;
        
        return isClosed;
    }
    
};