class Solution {
public:
    int minimumTime(vector<vector<int>>& grid) {
        if(grid[0][1] >= 2 && grid[1][0] >= 2){
            return -1;
        }
        
        int m = grid.size();
        int n = grid[0].size();
        
        using t_type = tuple<int, int, int>;
        priority_queue<t_type, vector<t_type>, greater<t_type>> pq;
        pq.push(make_tuple(0, 0, 0));
        
        while(pq.size() > 0){
            tuple<int, int, int> node = pq.top(); pq.pop();
            int t = get<0>(node);
            int x = get<1>(node);            
            int y = get<2>(node);
            
            if(grid[x][y] < 0){
                continue;
            }

            grid[x][y] = -1;
            
            if(x == m - 1 && y == n - 1){
                return t;
            }
            
            int arr[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
            for(auto [dx, dy]: arr){
                int nextX = x + dx;
                int nextY = y + dy;
                if(nextX < 0 || nextX >= m || nextY < 0 || nextY >= n || grid[nextX][nextY] < 0){
                    continue;
                }
                
                int waiting = grid[nextX][nextY] - t;
                if(waiting > 1){
                    waiting += waiting % 2 == 0;
                    pq.push(make_tuple(t + waiting, nextX, nextY));
                } else {
                    pq.push(make_tuple(t + 1, nextX, nextY));
                }
            }
        }
        
        return -1;

    }
};