class Solution {
public:
    int numSimilarGroups(vector<string>& strs) {
        int n = strs.size();
        unordered_map<int, vector<int>> graph;
        for(int node1 = 0; node1 < n; node1++){
            for(int node2 = node1 + 1; node2 < n; node2++){
                if(isSimilar(strs[node1], strs[node2])){
                    graph[node1].push_back(node2);
                    graph[node2].push_back(node1);
                }
            }
        }
        
        int ans = 0;
        vector<int> cache(n, -1);
        for(int node = 0; node < n; node++){
            if(cache[node] == -1){
                cache[node] = 0;
                recur(node, cache, graph);
                ans += 1;
            }
        }
        
        return ans;
    }
    
    void recur(int node, vector<int>& cache, unordered_map<int, vector<int>>& graph){
        for(int nextNode: graph[node]){
            if(cache[nextNode] == -1){
                cache[nextNode] = 0;
                recur(nextNode, cache, graph);
            }
        }
    }
    
    bool isSimilar(string s1, string s2){
        int n = s1.size();
        vector<int> idx;
        for(int i = 0; i < n; i++){
            if(s1[i] != s2[i]) idx.push_back(i);
        }
        
        if(idx.size() == 0){
            return true;
        } else if (idx.size() == 1 || idx.size() > 2){
            return false;
        }
        
        int i = idx[0], j = idx[1];
        return (s1[i] == s2[j] && s1[j] == s2[i]);
    }
    
};