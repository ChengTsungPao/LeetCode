class Solution {
public:
    int largestPathValue(string colors, vector<vector<int>>& edges) {
        
        int n = colors.size();
        int total_edge = 0;
        
        unordered_map<int, unordered_set<int>> graph;
        vector<int> parent(n, 0);
        for(int i = 0; i < edges.size(); i++){
            int node = edges[i][0], nextNode = edges[i][1];
            if(graph[node].find(nextNode) == graph[node].end()){
                graph[node].insert(nextNode);
                parent[nextNode] += 1;
                total_edge += 1;
            }
        }
        
        queue<int> q;
        vector<vector<int>> dp(n, vector(26, 0));
        for(int node = 0; node < n; node++){
            if(parent[node] == 0){
                dp[node][colors[node] - 'a'] += 1;
                q.push(node);
            }
        }
        
        int ans = 0;
        while(!q.empty()){
            int node = q.front(); q.pop();
            
            ans = max(ans, *max_element(dp[node].begin(), dp[node].end()));
            
            for(auto it = graph[node].begin(); it != graph[node].end(); it++){
                total_edge -= 1;
                int nextNode = *it;
                parent[nextNode] -= 1;

                for(int c = 0; c < 26; c++){
                    dp[nextNode][c] = max(dp[nextNode][c], dp[node][c] + (c == colors[nextNode] - 'a'));
                }

                if(parent[nextNode] == 0){
                    q.push(nextNode);
                }
            }
        }
        
        return (total_edge == 0) ? ans : -1;
    }
    
};