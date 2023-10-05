class UF {    
public:
    unordered_map<int, int> parent;
    unordered_map<int, int> weight;
    unordered_map<int, int> count;
    UF(){
        
    }
    
    void build(int node){
        if(parent.find(node) == parent.end()){
            parent[node] = node;
            weight[node] = 1;
            count[node] = 1;
        }
    }
    
    int findParent(int node){
        if(parent[node] == node){
            return node;
        }
        return parent[node] = findParent(parent[node]);
    }
    
    void _union(int node1, int node2){
        int p1 = findParent(node1), p2 = findParent(node2);
        
        if(p1 == p2){
            return;
        }
        
        if(weight[p1] < weight[p2]){
            parent[p2] = p1;
            count[p1] += count[p2];
        } else if (weight[p1] > weight[p2]){
            parent[p1] = p2;
            count[p2] += count[p1];
        } else {
            parent[p2] = p1;
            weight[p1] += 1;
            count[p1] += count[p2];
        }
    }
    
    int group(int node){
        if(parent.find(node) == parent.end()){
            return 1;
        }
        int p = findParent(node);
        return count[p];
    }
};


class Solution {
public:
    long long countPaths(int n, vector<vector<int>>& edges) {
        vector<bool> isPrime(n + 1, true);
        isPrime[0] = false;        
        isPrime[1] = false;
        for(int i = 2; i * i <= n; i++){
            if(isPrime[i]){
                for(int j = i * i; j <= n; j += i){
                    isPrime[j] = false;
                }
            }
        }
        
        UF uf;
        for(auto edge: edges){
            int u = edge[0], v = edge[1];
            if(!isPrime[u] && !isPrime[v]){
                uf.build(u);
                uf.build(v);
                uf._union(u, v);
            }
        }
        
        long long ans = 0;
        vector<long long> count(n + 1, 1);
        for(auto edge: edges){
            int u = edge[0], v = edge[1];
            if(isPrime[u] + isPrime[v] == 1){
                if(isPrime[u]) swap(u, v);
                ans += count[v] * uf.group(u);
                count[v] += uf.group(u);
            }
        }
        
        return ans;        
    }
};