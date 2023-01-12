class Solution {
public:
    vector<int> countSubTrees(int n, vector<vector<int>>& edges, string labels) {
        unordered_map<int, vector<int>> graph;
        for(int i = 0; i < edges.size(); i++){
            int node1 = edges[i][0], node2 = edges[i][1];
            graph[node1].push_back(node2);
            graph[node2].push_back(node1);
        }
        
        vector<int> ans(n, -1);
        recur(0, graph, labels, ans);
        return ans;
    }
    
    vector<int> recur(int node, unordered_map<int, vector<int>>& graph, string& labels, vector<int>& ans){
        char ch = labels[node];
        vector<int> count(26, 0);
        
        if(ans[node] >= 0){
            return count;
        }
        
        ans[node] = 0;
        
        count[ch - 'a'] += 1;
        for(int nextNode: graph[node]){
            vector<int> nextNodeCount = recur(nextNode, graph, labels, ans);
            for(int i = 0; i < nextNodeCount.size(); i++){
                count[i] += nextNodeCount[i];
            }           
        }
        
        ans[node] = count[ch - 'a'];
        return count;             
    }
};