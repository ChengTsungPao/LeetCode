class Solution {
public:
    int maximumDetonation(vector<vector<int>>& bombs) {
        int n = bombs.size();
        
        unordered_map<int, vector<int>> graph;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(i != j){
                    long long x1 = bombs[i][0], y1 = bombs[i][1], r1 = bombs[i][2];
                    long long x2 = bombs[j][0], y2 = bombs[j][1], r2 = bombs[j][2];
                    if((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) <= r1 * r1){
                        graph[i].push_back(j);
                    }
                }
            }
        }
        
        int ans = 0;
        for(int i = 0; i < n; i++){
            vector<bool> cache(n, false);
            ans = max(ans, recur(i, graph, cache));
        }
        
        return ans;
    }
    
    int recur(int i, unordered_map<int, vector<int>>& graph, vector<bool>& cache){   
        if(cache[i]){
            return 0;
        }
        cache[i] = true;

        int count = 1;
        for(int j: graph[i]){
            count += recur(j, graph, cache);
        }
        
        return count;
    }
    
};