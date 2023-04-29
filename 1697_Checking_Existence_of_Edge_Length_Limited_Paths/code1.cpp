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
    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList, vector<vector<int>>& queries) {
        
        vector<tuple<int, int, int>> edgeList_sort;
        for(int i = 0; i < edgeList.size(); i++){
            edgeList_sort.push_back({edgeList[i][2], edgeList[i][0], edgeList[i][1]});
        }
        
        vector<tuple<int, int, int, int>> queries_sort;
        for(int i = 0; i < queries.size(); i++){
            queries_sort.push_back({queries[i][2], queries[i][0], queries[i][1], i});
        }
        
        sort(edgeList_sort.begin(), edgeList_sort.end(), greater<>());
        sort(queries_sort.begin(), queries_sort.end());
        
        disjoint_set DS;
        vector<bool> ans(queries_sort.size(), false);
        for(int i = 0; i < queries_sort.size(); i++){
            tuple<int, int, int, int> t = queries_sort[i];
            int limit = get<0>(t), node1 = get<1>(t), node2 = get<2>(t), idx = get<3>(t);
            
            while(!edgeList_sort.empty() && get<0>(edgeList_sort.back()) < limit){
                tuple<int, int, int> t = edgeList_sort.back(); edgeList_sort.pop_back();
                int eLimit = get<0>(t), eNode1 = get<1>(t), eNode2 = get<2>(t);
                
                DS.build(eNode1);
                DS.build(eNode2);
                DS.Union(eNode1, eNode2);
            }
            
            ans[idx] = DS.isGroup(node1, node2);
        }
        
        return ans;
    }
};