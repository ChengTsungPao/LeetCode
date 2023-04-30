class disjoin_set {
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
        } else if (weight[p1] > weight[p2]){
            parent[p2] = p1;
        } else {
            parent[p1] = p2;
            weight[p2] += 1;
        }
    }
    
    bool isGroup(int node1, int node2){
        if(parent.find(node1) == parent.end() || parent.find(node2) == parent.end()){
            return false;
        }
        return findParent(node1) == findParent(node2);
    }
};

class Solution {
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        
        int ans = 0;
        disjoin_set DS1, DS2;
        for(int i = 0; i < edges.size(); i++){
            int type = edges[i][0], node1 = edges[i][1], node2 = edges[i][2];
            
            if(type == 3){
                if(DS1.isGroup(node1, node2)){
                    ans += 1;
                    continue;
                }
                
                DS1.build(node1);
                DS1.build(node2);
                DS1.Union(node1, node2);
                
                DS2.build(node1);
                DS2.build(node2);
                DS2.Union(node1, node2);
            }
        }
        
        for(int i = 0; i < edges.size(); i++){
            int type = edges[i][0], node1 = edges[i][1], node2 = edges[i][2];
            
            if(type == 1){
                if(DS1.isGroup(node1, node2)){
                    ans += 1;
                    continue;
                }
                
                DS1.build(node1);
                DS1.build(node2);
                DS1.Union(node1, node2);
                
            } else if (type == 2){
                if(DS2.isGroup(node1, node2)){
                    ans += 1;
                    continue;
                }                

                DS2.build(node1);
                DS2.build(node2);
                DS2.Union(node1, node2);
            }
        }
        
        int p1 = DS1.findParent(1), p2 = DS2.findParent(1);
        for(int node = 1; node <= n; node++){
            if(DS1.findParent(node) == -1 || DS2.findParent(node) == -1) return -1;
            if(DS1.findParent(node) != p1 || DS2.findParent(node) != p2) return -1;                
        }

        return ans;
    }
};