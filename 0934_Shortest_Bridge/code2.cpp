class Solution{
public:
    int shortestBridge(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        int isFind = false;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 1){
                    dfs(i, j, grid);
                    isFind = true;
                    break;
                }
            }
            if(isFind) break;
        }

        queue<pair<int, int>> q;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == -1){
                    q.push({i, j});
                }
            }
        }

        vector<vector<int>> dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        int length = 0;
        while(!q.empty()){
            queue<pair<int, int>> next_q;

            while(!q.empty()){
                pair<int, int> p = q.front(); q.pop();
                int i = p.first, j = p.second;
                for(auto& vec: dir){
                    int di = vec[0], dj = vec[1];
                    int x = i + di, y = j + dj;
                    if(x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == -1){
                        continue;
                    }
                    
                    if(grid[x][y] == 1){
                        return length;
                    }

                    next_q.push({x, y});
                    grid[x][y] = -1;
                }
            }
            length += 1;
            q = next_q;
        }

        return 0;
    }

    void dfs(int i, int j, vector<vector<int>>& grid){
        int m = grid.size();
        int n = grid[0].size();
        if(i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == -1 || grid[i][j] == 0){
            return;
        }
        grid[i][j] = -1;
        dfs(i + 1, j, grid);
        dfs(i, j + 1, grid);
        dfs(i - 1, j, grid);
        dfs(i, j - 1, grid);
    }
};