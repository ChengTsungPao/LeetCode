class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        int ans = 0;
        for(int i = 0; i < m; i++){
            int idx = upper_bound(grid[i].begin(), grid[i].end(), 0, [](int a, int b) {return a > b;}) - grid[i].begin();
            ans += n - idx;
        }
        
        return ans;
    }
};