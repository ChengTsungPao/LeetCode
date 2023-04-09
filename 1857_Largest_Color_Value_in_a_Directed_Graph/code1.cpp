class Solution {
public:
    int largestPathValue(string colors, vector<vector<int>>& edges) {
        
        int n = colors.size();
        int total_edge = 0;
        
        unordered_map<int, unordered_set<int>> graph;
        unordered_map<int, unordered_set<int>> rgraph;
        for(int i = 0; i < edges.size(); i++){
            int node = edges[i][0], nextNode = edges[i][1];
            if(graph[node].find(nextNode) == graph[node].end()){
                graph[node].insert(nextNode);
                rgraph[nextNode].insert(node);
                total_edge += 1;
            }
        }
        
        queue<tuple<int, vector<int>>> q;
        for(int node = 0; node < n; node++){
            if(rgraph[node].size() == 0){
                vector<int> count(26, 0);
                count[colors[node] - 'a'] += 1;
                q.push({node, count});
            }
        }
        
        int ans = 0;
        unordered_map<int, vector<vector<int>>> cache;
        while(!q.empty()){
            tuple<int, vector<int>> t = q.front(); q.pop();
            int node = get<0>(t);
            vector<int> count = get<1>(t);
            
            ans = max(ans, *max_element(count.begin(), count.end()));
            
            for(auto it = graph[node].begin(); it != graph[node].end(); it++){
                int nextNode = *it;
                
                // cache all path
                vector<int> copyCount = count;
                copyCount[colors[nextNode] - 'a'] += 1;
                cache[nextNode].push_back(copyCount);
                
                // remove nextNode parent
                if(rgraph[nextNode].find(node) != rgraph[nextNode].end()){
                    total_edge -= 1;
                    rgraph[nextNode].erase(node);
                }
                
                // update queue when nextNode do not have parent
                if(rgraph[nextNode].size() == 0){
                    while(!cache[nextNode].empty()){
                        vector<int> copyCount = cache[nextNode].back(); cache[nextNode].pop_back();
                        q.push({nextNode, copyCount});
                    }
                }
            }
        }

        return (total_edge == 0) ? ans : -1;
    }
};