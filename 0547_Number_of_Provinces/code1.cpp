class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool> cache(n, false);
        int ans = 0;
        for(int i = 0; i < n; i++){
            if(!cache[i]){
                recur(i, isConnected, cache);
                ans += 1;
            }
        }
        return ans;        
    }
    
    void recur(int i, vector<vector<int>>& isConnected, vector<bool>& cache) {
        int n = isConnected.size();
        if(cache[i]){
            return;
        }
        cache[i] = true;
        for(int j = 0; j < n; j++){
            if(isConnected[i][j] && i != j){
                recur(j, isConnected, cache);
            }
        }
        return;        
    }
    
};