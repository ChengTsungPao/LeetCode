class Solution {
public:
    long long countPairs(int n, vector<vector<int>>& edges) {
        
        // no edge
        if(edges.size() == 0){
            return (long long)(n) * (n - 1) / 2;
        }
        
        // create graph
        unordered_map<int, vector<int>> graph;
        for(int i = 0; i < edges.size(); i++){
            int node1 = edges[i][0], node2 = edges[i][1];
            graph[node1].push_back(node2);
            graph[node2].push_back(node1);
        }
        
        // count member
        vector<int> groups;
        vector<int> visited(n, false);
        for(int node = 0; node < n; node++){
            if(!visited[node]){
                int member = recur(node, visited, graph);
                groups.push_back(member);
            }
        }
        
        // count two member mul
        long long ans = 0, sum = 0;
        for(int member: groups){
            ans += sum * member;
            sum += member;
        }
        
        return ans;
    }
    
    int recur(int node, vector<int>& visited, unordered_map<int, vector<int>>& graph){
        if(visited[node]){
            return 0;
        }
        
        visited[node] = true;
        
        int member = 1;
        for(int nextNode: graph[node]){
            member += recur(nextNode, visited, graph);
        }
        
        return member;
    }
    
};