class UF{
public:
    vector<int> parent;
    vector<int> weight;
    
    UF(int n){
        parent.resize(n, -1);
        weight.resize(n, -1);
    }

    void build(int node){
        if(!exist(node)){
            parent[node] = node;
            weight[node] = 1;
        }
    }

    int findParent(int node){
        if(parent[node] == node){
            return node;
        }
        parent[node] = findParent(parent[node]);
        return parent[node];
    }

    void _union(int node1, int node2){
        int p1 = findParent(node1);
        int p2 = findParent(node2);

        if(p1 == p2){
            return;
        }

        if(weight[p1] < weight[p2]){
            parent[p1] = p2;
        } else if(weight[p1] > weight[p2]){
            parent[p2] = p1;
        } else {
            parent[p1] = p2;
            weight[p2] += 1;
        }
    }

    bool exist(int node){
        return parent[node] != -1;
    }
};

class Solution {
public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        int n = grid.size();
        if(grid[0][0] == 1 || grid[n - 1][n - 1] == 1){
            return 0;
        }
        
        unordered_map<int, vector<pair<int, int>>> factor;

        queue<pair<int, int>> q;
        vector<vector<bool>> cache(n, vector<bool>(n, false));
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n ; j++){
                if(grid[i][j] == 1){
                    q.push({i, j});
                    cache[i][j] = true;
                    factor[0].push_back({i, j});
                }
            }
        }

        int layer = 1;
        vector<vector<int>> dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        

        // bfs
        while(!q.empty()){
            queue<pair<int, int>> next_q;

            while(!q.empty()){
                pair<int, int> p = q.front(); q.pop();
                int i = p.first, j = p.second;

                for(auto vec: dir){
                    int di = vec[0], dj = vec[1];
                    int x = i + di, y = j + dj;
                    if(x >= 0 && x < n && y >= 0 && y < n && !cache[x][y]){
                        next_q.push({x, y});
                        factor[layer].push_back({x, y});
                        cache[x][y] = true;
                    }
                }
            }
            q = next_q;
            layer += 1;
        }


        // union find
        UF uf = UF(n * n);
        for(int f = layer - 1; f >= 0; f--){
            for(auto p: factor[f]){
                int i = p.first, j = p.second;
                int key1 = i * n + j;
                uf.build(key1);

                for(auto vec: dir){
                    int di = vec[0], dj = vec[1];
                    int x = i + di, y = j + dj;
                    if(x >= 0 && x < n && y >= 0 && y < n){
                        int key2 = x * n + y;
                        if(uf.exist(key2)){
                            uf._union(key1, key2);
                        }
                    }
                }

                if(uf.exist(0) && uf.exist(n * n - 1) && uf.findParent(0) == uf.findParent(n * n - 1)){
                    return f;
                }
            }
        }

        return -1;
    }
};