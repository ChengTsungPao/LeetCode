class Solution {
public:
    int minimumVisitedCells(vector<vector<int>>& grid) {
        
        int m = grid.size();
        int n = grid[0].size();
        
        queue<tuple<int, int, int>> q;
        q.push({0, 0, 1});
        
        vector<int> rowVector;
        for(int i = 0; i <= m; i++){
            rowVector.push_back(i);
        }
        vector<int> colVector;
        for(int j = 0; j <= n; j++){
            colVector.push_back(j);
        }
        
        vector<set<int>> rowCache(n, set<int>(rowVector.begin(), rowVector.end()));
        vector<set<int>> colCache(m, set<int>(colVector.begin(), colVector.end()));
        rowCache[0].erase(0);
        colCache[0].erase(0);
        
        while(!q.empty()){
            tuple<int, int, int> t = q.front(); q.pop();
            int i = get<0>(t), j = get<1>(t), step = get<2>(t);
            // cout << i << " " << j << " " << cache[1][4] << endl;
            if(i == m - 1 && j == n - 1){
                return step;
            }
            
            // rightward movement
            for(int k = j + 1; k <= min(grid[i][j] + j, n - 1); k++){
                if(colCache[i].find(k) != colCache[i].end()){
                    colCache[i].erase(k);
                    q.push({i, k, step + 1});
                } else {
                    k = *colCache[i].upper_bound(k) - 1;
                }
            }
            
            // downward movement
            for(int k = i + 1; k <= min(grid[i][j] + i, m - 1); k++){
                if(rowCache[j].find(k) != rowCache[j].end()){
                    rowCache[j].erase(k);
                    q.push({k, j, step + 1});
                } else {
                    k = *rowCache[j].upper_bound(k) - 1;
                }
            }            
        }
        
        return -1;
    }
};