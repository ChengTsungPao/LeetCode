class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        int ans = 0;
        int i = m - 1, j = 0;
        while(i >= 0 && j < n){
            if(grid[i][j] >= 0){
                j += 1;
            } else {
                i -= 1;
                ans += n - j;
            }
        }
        
        return ans;
    }
};