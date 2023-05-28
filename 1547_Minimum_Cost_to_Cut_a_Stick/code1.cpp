class Solution {
public:
    int minCost(int n, vector<int>& cuts) {
        vector<vector<int>> memo(n + 1, vector<int>(n + 1, -1));
        return recur(0, n, cuts, memo);
    }
    
    int recur(int i, int j, vector<int>& cuts, vector<vector<int>>& memo) {       
        if(memo[i][j] != -1){
            return memo[i][j];
        }
        
        int ans = INT_MAX;
        for(int k: cuts){
            if(i < k && k < j){
                ans = min(ans, recur(i, k, cuts, memo) + recur(k, j, cuts, memo) + (j - i));
            }
        }
        memo[i][j] = (ans != INT_MAX) ? ans : 0;
        return memo[i][j];
    }
    
};