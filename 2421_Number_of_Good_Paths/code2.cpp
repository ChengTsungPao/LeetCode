class disjoint_set {
public:
    unordered_map<int, int> parent;
    unordered_map<int, int> weight;
    
    void build(int node){
        if(parent.find(node) == parent.end()){
            parent[node] = node;
            weight[node] = 1;
        }
    }
    
    int findParent(int node){
        if(parent.find(node) == parent.end()){
            return -1;
        }
        if(parent[node] == node){
            return node;
        }
        parent[node] = findParent(parent[node]);
        return parent[node];
    }
    
    void Union(int node1, int node2){
        int p1 = findParent(node1);
        int p2 = findParent(node2);
        
        if(p1 == p2){
            return;
        }
        
        if(weight[p1] < weight[p2]){
            parent[p1] = p2;
        } else if (weight[p1] > weight[p2]) {
            parent[p2] = p1;
        } else {
            parent[p1] = p2;
            weight[p2] += 1;
        }
    }     
};

class Solution {
public:
    int numberOfGoodPaths(vector<int>& vals, vector<vector<int>>& edges) {
        int n = vals.size();
        
        unordered_map<int, vector<int>> valNode;
        vector<int> val_vector;
        for(int i = 0; i < n; i++){
            int val = vals[i];
            if(valNode.find(val) == valNode.end()){
                val_vector.push_back(val);
            }
            valNode[val].push_back(i);
        }
        sort(val_vector.begin(), val_vector.end());
        
        unordered_map<int, vector<tuple<int, int>>> valEdge;
        for(int i = 0; i < edges.size(); i++){
            int node1 = edges[i][0], node2 = edges[i][1];
            int maxVal = max(vals[node1], vals[node2]);
            valEdge[maxVal].push_back({node1, node2});
        }
        
        disjoint_set DS;
        
        int ans = n;
        for(int i = 0; i < val_vector.size(); i++){
            int val = val_vector[i];
            
            // visited node & build node
            for(int j = 0; j < valNode[val].size(); j++){
                int node = valNode[val][j];
                DS.build(node);
            }
            
            // visited edge & union node
            for(int j = 0; j < valEdge[val].size(); j++){
                tuple<int, int> t = valEdge[val][j];
                int node1 = get<0>(t), node2 = get<1>(t);
                DS.Union(node1, node2);
            }

            // count group member
            unordered_map<int, int> count;
            for(int j = 0; j < valNode[val].size(); j++){
                int node = valNode[val][j];
                int p = DS.findParent(node);
                count[p] += 1;
            }
            
            // calculate ans
            for(auto& [k, v]: count){
                ans += v * (v - 1) / 2;
            }
            
        }
        
        return ans;
    }
};