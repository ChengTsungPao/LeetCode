class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        
        // create graph
        unordered_map<int, vector<int>> graph;
        vector<int> graph_n(n, -1);
        for(int i = 0; i < connections.size(); i++){
            int node1 = connections[i][0], node2 = connections[i][1];
            graph[node1].push_back(node2);
            graph[node2].push_back(node1);
        }
        
        // traversal tree
        unordered_map<int, unordered_set<int>> visitedEdge;
        unordered_set<int> visitedNode;
        visitedNode.insert(0);
        recur(0, visitedNode, visitedEdge, graph);
        
        // count reverse roads by visitedEdge
        int ans = 0;
        for(int i = 0; i < connections.size(); i++){
            int node1 = connections[i][0], node2 = connections[i][1];
            if(visitedEdge.count(node1) > 0 && visitedEdge[node1].count(node2) > 0){
                ans += 1;
            }
        }
        
        return ans;
    }
    
    void recur(int node, unordered_set<int>& visitedNode, unordered_map<int, unordered_set<int>>& visitedEdge, unordered_map<int, vector<int>>& graph){
        
        for(int nextNode: graph[node]){
            if(visitedNode.count(nextNode) > 0){
                continue;
            }
            
            visitedNode.insert(nextNode);
            visitedEdge[node].insert(nextNode);
            recur(nextNode, visitedNode, visitedEdge, graph);
        }
    }
    
    
};