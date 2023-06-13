class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        int n = grid.size();
        
        unordered_map<string, int> countRow, countCol;
        for(int i = 0; i < n; i++){
            string rowArr = to_string(grid[i][0]), colArr = to_string(grid[0][i]);
            for(int j = 1; j < n; j++){
                rowArr += "," + to_string(grid[i][j]);
                colArr += "," + to_string(grid[j][i]);
            }
            countRow[rowArr] += 1;
            countCol[colArr] += 1;
        }
        
        int ans = 0;
        for(auto& [k, v]: countRow){
            ans += v * countCol[k];
        }
        
        return ans;
    }
};