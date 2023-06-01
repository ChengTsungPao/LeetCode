class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        
        if(grid[0][0] == 1) {
            return -1;
        }
        
        int n = grid.size();
        
        queue<tuple<int, int, int>> q;
        q.push({0, 0, 0});
        grid[0][0] = 1;
        
        while(!q.empty()) {
            tuple<int, int, int> t = q.front(); q.pop();
            int x = get<0>(t), y = get<1>(t), step = get<2>(t);
            
            if(x == n - 1 && y == n - 1) {
                return step + 1;
            }
            
            for(int dx: {-1, 0, 1}){
                for(int dy: {-1, 0, 1}){
                    int x_ = x + dx, y_ = y + dy;
                    if(x_ < 0 || x_ >= n || y_ < 0 || y_ >= n || grid[x_][y_] == 1){
                        continue;
                    }
                    
                    grid[x_][y_] = 1;
                    q.push({x_, y_, step + 1});
                }
            }
        }
        
        return -1;
    }
};