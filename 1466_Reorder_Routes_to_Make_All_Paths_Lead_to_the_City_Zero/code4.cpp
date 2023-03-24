class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        
        // create graph
        unordered_map<int, vector<tuple<int, int>>> graph;
        for(int i = 0; i < connections.size(); i++){
            int node1 = connections[i][0], node2 = connections[i][1];
            graph[node2].push_back({node1, 0});
            graph[node1].push_back({node2, 1});
        }
        
        // traversal tree
        vector<int> visited(n, false);
        visited[0] = true;
        return recur(0, visited, graph);
    }
    
    int recur(int node, vector<int>& visited, unordered_map<int, vector<tuple<int, int>>>& graph){
        int ans = 0;
        for(auto& [nextNode, target]: graph[node]){
            if(!visited[nextNode]){
                visited[nextNode] = true;
                ans += target + recur(nextNode, visited, graph);
            }
        }
        return ans;
    }
};