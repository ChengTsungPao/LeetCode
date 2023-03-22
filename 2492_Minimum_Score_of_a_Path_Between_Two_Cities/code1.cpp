class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        
        unordered_map<int, vector<int>> graph;
        for(int i = 0; i < roads.size(); i++){
            int node = roads[i][0], nextNode = roads[i][1];
            graph[node].push_back(nextNode);           
            graph[nextNode].push_back(node);
        }
        
        unordered_set<int> visited;
        recur(1, graph, visited);
        
        int ans = INT_MAX;
        for(int i = 0; i < roads.size(); i++){
            int node = roads[i][0], nextNode = roads[i][1], score = roads[i][2];
            if(visited.count(node) || visited.count(nextNode)){
                ans = min(ans, score);
            }
        }
        
        return ans;
    }
    
    void recur(int node, unordered_map<int, vector<int>>& graph, unordered_set<int>& visited){
        if(visited.count(node)){
            return;
        }
        
        visited.insert(node);
        
        for(int nextNode: graph[node]){
            recur(nextNode, graph, visited);
        }
    }
};