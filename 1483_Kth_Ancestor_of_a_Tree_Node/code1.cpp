class TreeAncestor {
public:
    unordered_map<int, vector<int>> ancestor;
    TreeAncestor(int n, vector<int>& parent) {
        for(int node = 0; node < n; node++){
            getAncestor(node, parent);
        }
    }
    
    int getKthAncestor(int node, int k) {
        return (this -> ancestor[node].size() >= k) ? this -> ancestor[node][k - 1] : -1;
    }
    
    vector<int> getAncestor(int node, vector<int>& parent){
        if(this -> ancestor.count(node)){
            return this -> ancestor[node];
        }
        
        if(node == -1){
            return {};
        }
        
        vector<int> ans = getAncestor(parent[node], parent);
        ans.insert(ans.begin(), parent[node]);
        this -> ancestor[node] = ans;
        return ans;
    }
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor* obj = new TreeAncestor(n, parent);
 * int param_1 = obj->getKthAncestor(node,k);
 */