class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<vector<vector<int>>>> memo(n + 1, vector<vector<vector<int>>>(k + 1, vector<vector<int>>(0)));
        return recur(n, k, memo);
    }
    
    vector<vector<int>> recur(int n, int k, vector<vector<vector<vector<int>>>>& memo) {
        if(k == 0){
            return {{}};
        }
        
        if(!memo[n][k].empty()){
            return memo[n][k];
        }
        
        vector<vector<int>> ans;
        if(n > k){
            ans = recur(n - 1, k, memo);
        }
        
        for(auto ret: recur(n - 1, k - 1, memo)){
            ret.push_back(n);
            ans.push_back(ret);
        }
        
        memo[n][k] = ans;
        return ans;
    }
    
};