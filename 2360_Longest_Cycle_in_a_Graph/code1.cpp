class Solution {
public:
    int ans = -1;
    
    int longestCycle(vector<int>& edges) {
        int n = edges.size();
        vector<bool> cache(n, false);
        
        for(int node = 0; node < n; node++){
            unordered_map<int, int> targets;
            recur(node, 0, targets, cache, edges);
            
            for(auto it = targets.begin(); it != targets.end(); it++){
                cache[it -> first] = true;
            }
        }
        return ans;
    }
    
    void recur(int node, int target, unordered_map<int, int>& targets, vector<bool>& cache, vector<int>& edges){
        int nextNode = edges[node];
        
        if(cache[node] || nextNode == -1){
            return;
        } else if(targets.find(nextNode) != targets.end()){
            int cycle = target - targets[nextNode] + 1;
            ans = (ans < cycle && cycle > 0) ? cycle : ans;
            return;
        }
        
        targets[node] = target;
        recur(nextNode, target + 1, targets, cache, edges);
    }
};